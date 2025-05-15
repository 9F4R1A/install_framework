import subprocess

def check_repo(repo):
    output = subprocess.check_output("dnf repolist", shell=True)
    output = str(output)
    output = output.find(repo)
    if output >= 0:
        return 0
    else:
        return 1