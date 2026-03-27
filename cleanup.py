import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")
OWNER = os.getenv("REPO_OWNER")
REPO = os.getenv("REPO_NAME")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}"
}

# Set stale threshold (for testing keep 0 or 1 day)
STALE_DAYS = 0

def get_branches():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/branches"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching branches:", response.json())
        return []

def get_last_commit_date(branch):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/commits/{branch}"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 200:
        data = response.json()
        date_str = data['commit']['committer']['date']
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
    else:
        print(f"Error fetching commit for {branch}")
        return None

def delete_branch(branch):
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/git/refs/heads/{branch}"
    response = requests.delete(url, headers=HEADERS)
    
    if response.status_code == 204:
        print(f"Deleted branch: {branch}")
    else:
        print(f"Failed to delete {branch}: {response.json()}")

if __name__ == "__main__":
    branches = get_branches()
    now = datetime.utcnow()

    for branch in branches:
        name = branch["name"]

        if name == "main":
            continue

        last_commit = get_last_commit_date(name)

        if last_commit:
            diff = now - last_commit

            if diff > timedelta(days=STALE_DAYS):
                print(f"Stale branch found: {name}")
                delete_branch(name)
            else:
                print(f"{name} is active")