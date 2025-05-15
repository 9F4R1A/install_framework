import subprocess

def move_file(file_in,file_out):
    output = subprocess.run(["mv", file_in, file_out])
    return output.returncode