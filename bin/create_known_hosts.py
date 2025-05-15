import os

def create_known_hosts():
    file_name = "/root/.ssh/known_hosts"
    filedata = "" # put your known host here
    try:
        with open(file_name, 'w') as infile:
            infile.write(filedata)
            os.chmod(file_name,0o600)
            return 0
    except OSError:
        print ("Could not open/read file:", file_name)
        return 1