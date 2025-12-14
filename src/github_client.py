import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

def get_repo_data(url):
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN not found in .env file")
    
    g = Github(token)
    
    try:
        # Extract owner/repo (e.g., "rahul-dev/todo" from url)
        clean_url = url.replace("https://github.com/", "").strip("/")
        repo = g.get_repo(clean_url)
        return repo
    except Exception as e:
        print(f"Error fetching repo: {e}")
        return None

def get_file_content(repo, path):
    try:
        content = repo.get_contents(path)
        return content.decoded_content.decode("utf-8")
    except:
        return None