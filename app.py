import streamlit as st
from src.github_client import get_repo_data, get_file_content
from src.analysis import calculate_score
from src.ai_agent import get_ai_feedback

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="GitGrade", page_icon="📊", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    .stAlert {
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("📊 GitGrade: AI-Powered Repository Auditor")
st.markdown("### Evaluate your code quality, structure, and readiness for recruitment.")

# --- INPUT SECTION ---
url = st.text_input("🔗 Paste GitHub Repository URL:", placeholder="https://github.com/username/project-name")

if st.button("Analyze Repository"):
    if not url:
        st.warning("Please enter a URL.")
    else:
        with st.spinner("🔍 Cloning metadata and analyzing structure..."):
            repo = get_repo_data(url)
            
            if not repo:
                st.error("Could not access repository. Make sure it is public and the URL is correct.")
            else:
                # 1. Gather Data (Files & Content)
                try:
                    contents = repo.get_contents("")
                    file_tree = [c.path for c in contents]
                    
                    # Dig one level deeper to find more files
                    while contents:
                        file_content = contents.pop(0)
                        if file_content.type == "dir":
                            try:
                                items = repo.get_contents(file_content.path)
                                contents.extend(items)
                                for item in items:
                                    file_tree.append(item.path)
                            except:
                                pass # Skip inaccessible folders
                except Exception as e:
                    st.error(f"Error reading file structure: {e}")
                    file_tree = []
                
                readme_content = get_file_content(repo, "README.md") or ""

                # 2. Run Analysis (Math + AI)
                score, breakdown = calculate_score(repo, file_tree, readme_content)
                ai_data = get_ai_feedback(repo.name, file_tree, readme_content)

                # 3. DISPLAY RESULTS
                st.divider()
                
                # --- Top Dashboard ---
                col1, col2, col3 = st.columns([1, 2, 1])
                
                with col1:
                    st.metric("GitGrade Score", f"{score}/100")
                
                with col2:
                    st.subheader("🤖 AI Summary")
                    # Error Handling: Check if AI returned an error
                    if "error" in ai_data:
                        st.error(f"AI Error: {ai_data['error']}")
                    else:
                        st.info(ai_data.get("summary", "No summary available."))

                with col3:
                    if score >= 80:
                        st.balloons()
                        st.success("Result: Excellent!")
                    elif score >= 50:
                        st.warning("Result: Average")
                    else:
                        st.error("Result: Needs Work")

                # --- Detailed Breakdown ---
                st.divider()
                col_left, col_right = st.columns(2)
                
                with col_left:
                    st.subheader("🚧 Rule-Based Checks")
                    if breakdown:
                        for issue, advice in breakdown.items():
                            st.write(f"❌ **{issue}**: {advice}")
                    else:
                        st.success("✅ No critical structural issues found!")

                with col_right:
                    st.subheader("🗺️ Personalized Roadmap")
                    
                    roadmap_items = ai_data.get("roadmap", [])
                    
                    # Check if roadmap is valid list
                    if isinstance(roadmap_items, list) and len(roadmap_items) > 0:
                        for item in roadmap_items:
                            # Extract data safely with defaults
                            phase = item.get("phase", "General")
                            task = item.get("task", "Task")
                            detail = item.get("detail", "No details provided.")
                            
                            # Color coding based on phase
                            color = "#FF4B4B"  # Red for Immediate
                            if "Short" in phase: color = "#FFA500" # Orange
                            if "Medium" in phase: color = "#17a2b8" # Blue
                            if "Long" in phase: color = "#28a745"  # Green

                            # Render the Card (HTML/CSS)
                            st.markdown(f"""
                            <div style="
                                border-left: 5px solid {color};
                                background-color: #f9f9f9;
                                padding: 15px;
                                margin-bottom: 10px;
                                border-radius: 5px;
                                box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
                            ">
                                <strong style="color: {color}; text-transform: uppercase; font-size: 0.8em;">{phase}</strong>
                                <h4 style="margin: 5px 0 10px 0; color: #333;">{task}</h4>
                                <p style="margin: 0; color: #666; font-size: 0.95em;">{detail}</p>
                            </div>
                            """, unsafe_allow_html=True)
                    else:
                        # If list is empty or invalid
                        if "error" not in ai_data:
                            st.info("No specific roadmap generated.")