#!/usr/bin/env python3
import subprocess
import os
from pathlib import Path

REPOS_FILE = "repos.txt"

def run(cmd, cwd=None):
    """Run a shell command cross-platform and print output."""
    print(f"$ {' '.join(cmd)} (cwd={cwd})")
    result = subprocess.run(cmd, cwd=cwd, check=True)
    return result.returncode

def sync_repo(url, branch="main"):
    """Clone or pull the repo."""
    name = Path(url).stem
    repo_path = Path(name)
    if repo_path.exists() and (repo_path / ".git").exists():
        print(f"Updating {name}...")
        run(["git", "fetch", "origin"], cwd=name)
        run(["git", "checkout", branch], cwd=name)
        run(["git", "pull"], cwd=name)
    else:
        print(f"Cloning {name}...")
        run(["git", "clone", "--branch", branch, url])

def main():
    if not Path(REPOS_FILE).exists():
        print(f"{REPOS_FILE} not found!")
        return

    with open(REPOS_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            url = parts[0]
            branch = parts[1] if len(parts) > 1 else "main"
            sync_repo(url, branch)

if __name__ == "__main__":
    main()
