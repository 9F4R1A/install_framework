import subprocess

def set_timezone():
    output = subprocess.run(["timedatectl", "set-timezone", "Etc/UTC"])
    return output.returncode