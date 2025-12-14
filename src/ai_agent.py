import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_ai_feedback(repo_name, file_tree, readme_content):
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        return {"error": "Missing OpenAI API Key in .env file"}

    client = OpenAI(api_key=api_key)

    # Construct the prompt
    system_prompt = "You are a Senior Software Engineer acting as a mentor. You output strict JSON."
    
    user_prompt = f"""
    Analyze this GitHub repository context:
    
    Repo Name: {repo_name}
    File Structure: {str(file_tree[:60])} (truncated)
    README Snippet: {readme_content[:1500] if readme_content else "None"}

    Task:
    1. Write a summary (2 sentences) of the code quality.
    2. Create a roadmap of 3-4 specific technical improvements.
    
    Output Format (JSON):
    {{
        "summary": "...",
        "roadmap": [
            {{ "phase": "Immediate", "task": "...", "detail": "..." }},
            {{ "phase": "Short-Term", "task": "...", "detail": "..." }}
        ]
    }}
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"}, # This guarantees valid JSON
            temperature=0.7
        )
        
        # Parse the JSON string from OpenAI
        content = response.choices[0].message.content
        return json.loads(content)

    except Exception as e:
        return {"error": f"OpenAI Error: {str(e)}", "roadmap": []}