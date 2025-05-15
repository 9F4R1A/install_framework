import subprocess
import configparser
from bin.file_text_insert import file_text_insert

config = configparser.ConfigParser()
config.sections()
config.read('conf/install.cfg')

def install_package(package):
    logfile = config['generic']['logfile']
    file_text_insert(logfile,"installing " + package )
    output = subprocess.run(["dnf", "install", "-qy", package], capture_output = True, text = True)
    stdout = str(output.stdout)
    stderr = str(output.stderr)
    file_text_insert(logfile,stdout + stderr)
    return output.returncode