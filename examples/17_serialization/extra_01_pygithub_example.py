from github import Github
import os

username = ""
token = os.environ.get("GITHUB_TOKEN")
repo_name = "" # "natenka/pyneng-cli-course"

g = Github(username, token)
repo = g.get_repo(repo_name)
commits = repo.get_commits()
last = commits[0]
last.create_comment("TEST")

