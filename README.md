# Git Branch Cleanup Automation

## About
This project automatically deletes stale (unused) branches from a GitHub repository to keep it clean and organized.

---

## How It Works
- Connects to GitHub using API  
- Fetches all branches  
- Checks last commit activity  
- Deletes inactive branches (except main)  

---

## Tech Stack
- Python  
- GitHub API  
- GitHub Actions  

---

## How to Run

### Locally
1. Install dependencies:
   pip install requests python-dotenv  

2. Create `.env` file:
   GITHUB_TOKEN=your_token  
   REPO_OWNER=your_username  
   REPO_NAME=your_repo  

3. Run:
   python cleanup.py  

---

### Using GitHub Actions
- Go to **Actions tab**
- Click **Run workflow**

---

## Note
- `main` branch is safe (not deleted)  
- Stale time is set to 0 days for testing  
- Change it to 30 days for real use  

---

## Learning
- GitHub API usage  
- Automation with GitHub Actions  
- Real-world DevOps practice  

---

## Author
Tanima Mishra
