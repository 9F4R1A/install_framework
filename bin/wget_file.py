import subprocess
import configparser
from bin.file_text_insert import file_text_insert

config = configparser.ConfigParser()
config.sections()
config.read('conf/install.cfg')

def wget_file(url,local_dir):
    logfile = config['generic']['logfile']
    output = subprocess.run(["wget", url , "-q", "-P", local_dir ], capture_output = True, text = True)
    stdout = str(output.stdout)
    stderr = str(output.stderr)
    file_text_insert(logfile,stdout + stderr)
    return output.returncode