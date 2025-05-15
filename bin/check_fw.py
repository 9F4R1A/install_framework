import subprocess

def check_fw(port):
    output = subprocess.check_output("firewall-cmd --list-all --zone=work|grep \" ports:\"", shell=True)
    output = str(output)
    output = output.find(port)
    if output >= 0:
        return 0
    else:
        return 1