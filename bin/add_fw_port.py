import subprocess
import configparser
from bin.file_text_insert import file_text_insert

config = configparser.ConfigParser()
config.sections()
config.read('conf/install.cfg')

def add_fw_port(port,type):
    logfile = config['generic']['logfile']
    output = subprocess.run(["firewall-cmd", "--zone=work", "--add-port=" + port + "/" + type , "--permanent"], capture_output = True, text = True)
    stdout = str(output.stdout)
    stderr = str(output.stderr)
    file_text_insert(logfile,stdout + stderr)
    output_reload = subprocess.run(["firewall-cmd", "--reload"], capture_output = True, text = True)
    stdout_reload = str(output_reload.stdout)
    stderr_reload = str(output_reload.stderr)
    file_text_insert(logfile,stdout_reload + stderr_reload)
    return output.returncode