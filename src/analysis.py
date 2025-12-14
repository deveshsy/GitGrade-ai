def calculate_score(repo, file_tree_names, readme_content):
    score = 0
    breakdown = {}

    # 1. Documentation (25 pts)
    if readme_content:
        score += 10
        if len(readme_content) > 500: 
            score += 15
        else: 
            breakdown['Short Readme'] = "README is too short to be useful."
    else:
        breakdown['Missing Readme'] = "Crucial! Add a README.md."

    # 2. Structure & Best Practices (25 pts)
    if ".gitignore" in file_tree_names: 
        score += 10
    else: 
        breakdown['No .gitignore'] = "Add .gitignore to keep repo clean."
    
    # Check for dependency files
    if any(f in file_tree_names for f in ["requirements.txt", "package.json", "pom.xml", "go.mod"]): 
        score += 15
    else:
        breakdown['No Dependencies'] = "List dependencies (requirements.txt/package.json)."

    # 3. Testing (25 pts)
    # Check for test folders or files like test_*.py, *.test.js
    has_tests = any("test" in f.lower() for f in file_tree_names)
    if has_tests: 
        score += 25
    else: 
        breakdown['No Tests'] = "No testing framework detected."

    # 4. Activity/Git Health (25 pts)
    # Real repos have history. Dummy repos have 1 commit.
    if repo.get_commits().totalCount > 5: 
        score += 25
    else: 
        breakdown['Low Activity'] = "Very few commits. Commit early and often."

    return score, breakdown