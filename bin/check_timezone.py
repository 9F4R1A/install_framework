import subprocess

def check_timezone():
    output = subprocess.check_output("timedatectl| grep zone", shell=True)
    output = str(output)
    
    if output[29:36] == "Etc/UTC":
        return 0
    else:
        return 1