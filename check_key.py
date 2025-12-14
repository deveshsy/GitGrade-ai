import os
from dotenv import load_dotenv

# 1. Try to load the file
loaded = load_dotenv()

# 2. Check the results
print("--- DEBUGGING KEYS ---")
print(f"1. Did python-dotenv find a .env file? -> {loaded}")

key = os.getenv("OPENAI_API_KEY")
if key:
    print(f"2. Key Found! Length: {len(key)} characters.")
    print(f"3. Starts with: {key[:5]}...")
else:
    print("2. RESULT: Key is None. The file is missing or the variable name is wrong.")