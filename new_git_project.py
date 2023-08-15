import os

git_nick_name = 'gabflag'
repository_name = input("Repository name: ")

list_of_commands = [
    f'mkdir {repository_name}',
    f'echo "# {repository_name}" >> {repository_name}\\README.md',
    f'cd {repository_name} && git init',
    f'cd {repository_name} && git add README.md',
    f'cd {repository_name} && echo "venv" > .gitignore',
    f'cd {repository_name} && git commit -m "first commit"',
    f'cd {repository_name} && git branch -M main',
    f'cd {repository_name} && git remote add origin https://github.com/{git_nick_name}/{repository_name}.git',
    f'cd {repository_name} && git push -u origin main',
]

for command in list_of_commands:
    os.system(command)
