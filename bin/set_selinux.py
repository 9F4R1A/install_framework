import subprocess
from .file_text_replace import file_text_replace

def set_selinux():
    output = subprocess.run(["setenforce", "0"])
    file_text_replace("/etc/selinux/config","SELINUX=enforcing","SELINUX=permissive")
    return output.returncode