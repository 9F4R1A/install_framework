import subprocess

def link_file(origin,link):
    output = subprocess.run(["ln", "-s", origin , link ])
    return output.returncode