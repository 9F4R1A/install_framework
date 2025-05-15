import os
import subprocess
import configparser
from bin.file_text_insert import file_text_insert

config = configparser.ConfigParser()
config.sections()
config.read('conf/install.cfg')

def gunzip(infile, tofile):
    logfile = config['generic']['logfile']
    
    file_name = "temp_exec.sh"
    try:
        # Read in the file
        with open(file_name, 'a') as file:
            file.write("gunzip -c " + infile + " > " + tofile)
    except OSError:
        print ("Could not open/read file:", file_name)
    os.chmod(file_name,0o700)
    output = subprocess.check_output("./" + file_name + " 2>/dev/null", shell=True )
    output = output.decode('utf-8')

    file_text_insert(logfile,output)

    os.system("rm -rf " + file_name)
