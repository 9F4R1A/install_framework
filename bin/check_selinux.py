import subprocess

def check_selinux():
    output = subprocess.check_output("getenforce", shell=True)
    output = str(output)
    output = output[2:12]
    
    if output == "Permissive":
        return 0
    else:
        return 1