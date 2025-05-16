import subprocess

def check_host(host):
    output = subprocess.check_output("firewall-cmd --list-all --zone=work|grep \" sources:\"", shell=True)
    output = str(output)
    output = output.find(host)
    if output >= 0:
        return 0
    else:
        return 1