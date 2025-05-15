import subprocess
from .file_text_insert import file_text_insert

def set_hostname(hostname,ip,domain):
    output = subprocess.run(["hostnamectl", "set-hostname", hostname])
    output = output.returncode + file_text_insert("/etc/hosts", ip + " " + hostname + " " + hostname + "." + domain + "\n")
    return output
