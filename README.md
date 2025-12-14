# 📊 GitGrade: AI-Powered Repository Auditor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gitgrade.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/AI-GPT--4o--Mini-green)](https://openai.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**GitGrade** is an intelligent developer profiling tool designed to evaluate GitHub repositories. It acts as an automated "Senior Developer Mentor," analyzing code quality, structure, and documentation to provide students with a meaningful score and an actionable roadmap for improvement.

Built for the **UnsaidTalks GitGrade Hackathon** (Theme: AI + Code Analysis).

---

## 🚀 Live Demo
### [👉 Click here to try GitGrade Live](https://gitgrade.streamlit.app/)

---

## 🎯 Problem It Solves
Students often upload code to GitHub without knowing if it looks "professional" to recruiters. GitGrade bridges this gap by:
1.  **Scoring:** mathematically evaluating the repo based on industry standards (Tests, CI/CD, Documentation).
2.  **Summarizing:** Using **GPT-4o** to read the code context and explain what the project actually does.
3.  **Mentoring:** Generating a personalized, phase-based roadmap (Immediate vs. Long-term goals) to improve the code.

## 🛠️ Tech Stack
* **Frontend:** [Streamlit](https://streamlit.io/) (Rapid UI Development)
* **Backend Logic:** Python
* **AI Engine:** OpenAI GPT-4o-mini (JSON Mode for structured output)
* **Data Fetching:** PyGithub (GitHub API)
* **Analysis:** Custom rule-based heuristics + LLM qualitative analysis

## 📸 Screenshots

*<img width="2846" height="1444" alt="image" src="https://github.com/user-attachments/assets/63e3edc9-9bf0-491d-a203-75e5f77edd99" />
*

## ⚡ Features
* **✅ GitGrade Score (0-100):** Real-time calculation based on file existence (`README.md`, `.gitignore`, `requirements.txt`) and testing frameworks.
* **🤖 AI Analysis:** Generates a 2-sentence executive summary of the codebase.
* **🗺️ Dynamic Roadmap:** A card-based UI distinguishing between "Immediate Fixes" and "Long-term Architecture" improvements.
* **🔍 Deep Search:** Recursively analyzes file trees to understand project complexity.

## 💻 How to Run Locally

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/deveshsy/GitGrade-ai.git](https://github.com/deveshsy/GitGrade-ai.git)
    cd GitGrade-ai
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Keys**
    Create a `.env` file in the root directory:
    ```env
    GITHUB_TOKEN=your_github_pat_token
    OPENAI_API_KEY=your_openai_api_key
    ```

4.  **Run the App**
    ```bash
    streamlit run app.py
    ```

## 📂 Project Structure
```text
GitGrade-AI/
├── app.py                # Main Streamlit Dashboard entry point
├── requirements.txt      # Project dependencies
├── .env                  # API Secrets (Not committed)
└── src/
    ├── analysis.py       # Mathematical scoring logic
    ├── ai_agent.py       # OpenAI GPT-4o integration
    └── github_client.py  # GitHub API handler
