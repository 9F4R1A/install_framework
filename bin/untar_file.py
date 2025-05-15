import subprocess
import configparser
from bin.file_text_insert import file_text_insert

config = configparser.ConfigParser()
config.sections()
config.read('conf/install.cfg')

def untar_file(file,indir,outdir):
    logfile = config['generic']['logfile']
    output = subprocess.run(["tar", "zxf", indir + "/" + file, "-C", outdir ], capture_output = True, text = True)
    stdout = str(output.stdout)
    stderr = str(output.stderr)
    file_text_insert(logfile,stdout + stderr)
    return output.returncode