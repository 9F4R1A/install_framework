import os

def make_dir(dir):
    check_exist = os.path.isdir(dir)
    if not check_exist:
        os.makedirs(dir)