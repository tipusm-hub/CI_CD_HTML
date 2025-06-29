
import subprocess
import os
#import git

repo_path = "/home/lenovo/B12/git_repo/CI_CD_HTML"

def check_for_new_commits_subprocess(repo_path):
    """Checks if there are new commits using Git commands via subprocess."""
    try:
        # Change directory to the repository path
        os.chdir(repo_path)

        # Fetch latest changes
        subprocess.run(["git", "fetch"], check=True)

        # Check status
        status_output = subprocess.check_output(["git", "status", "-uno"], text=True).strip()

        if "Your branch is up to date" in status_output:
            print(f"Repository '{repo_path}' is up to date.")
        elif "Your branch is behind" in status_output:
            print(f"New commits found in '{repo_path}'.")
        else:
            print(f"Could not determine status for '{repo_path}'.")

    except FileNotFoundError:
        print("Error: Git command not found. Make sure Git is installed and in your PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing Git command: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    repository_path = "/home/lenovo/B12/git_repo/CI_CD_HTML"  # Replace with the actual path
    check_for_new_commits_subprocess(repository_path)
