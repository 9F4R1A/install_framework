import subprocess
import configparser
from bin.file_text_insert import file_text_insert

config = configparser.ConfigParser()
config.sections()
config.read('conf/install.cfg')

def check_package(package):
    output = subprocess.run(["dnf", "list", "installed", package], capture_output = True, text = True)
    return output.returncode
