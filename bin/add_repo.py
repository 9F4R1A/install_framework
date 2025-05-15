import subprocess
import configparser
from bin.file_text_insert import file_text_insert

config = configparser.ConfigParser()
config.sections()
config.read('conf/install.cfg')

def add_repo(repo):
    logfile = config['generic']['logfile']
    if repo == "epel":
        output = subprocess.run(["dnf", "install", "-y", repo + "-release"], capture_output = True, text = True)
        stdout = str(output.stdout)
        stderr = str(output.stderr)
        file_text_insert(logfile,stdout + stderr)
        return output.returncode
    elif repo == "docker":
        output = subprocess.run(["dnf", "config-manager", "--add-repo", "https://download.docker.com/linux/centos/docker-ce.repo"], capture_output = True, text = True)
        stdout = str(output.stdout)
        stderr = str(output.stderr)
        file_text_insert(logfile,stdout + stderr)
        return output.returncode
    else:
        return 1