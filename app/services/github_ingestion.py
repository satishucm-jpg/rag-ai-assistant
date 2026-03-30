import os
from git import Repo
from langchain_community.document_loaders import TextLoader

CLONE_DIR = "repo"

def clone_repo(repo_url):
    if os.path.exists(CLONE_DIR):
        return CLONE_DIR
    
    Repo.clone_from(repo_url, CLONE_DIR)
    return CLONE_DIR


def load_repo_files(repo_path):
    documents = []
    max_files = 50
    count = 0

    for root, _, files in os.walk(repo_path):
        for file in files:

            if count >= max_files:
                break

            if file.endswith((".py", ".md")):
                file_path = os.path.join(root, file)

                if any(skip in file_path for skip in ["venv", "node_modules", ".git", "__pycache__"]):
                    continue

                try:
                    loader = TextLoader(file_path, encoding="utf-8")
                    documents.extend(loader.load())
                    count += 1
                except:
                    continue

    return documents