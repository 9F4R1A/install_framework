import os

def check_file(file_name,filedata_check):

    # Read in the file
    try:
        with open(file_name, 'r') as file:
            filedata = file.read()
        if filedata == filedata_check:
            return 0
    except OSError:
        return 1