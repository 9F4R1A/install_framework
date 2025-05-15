

def file_text_replace (file_name,file_search,file_replace):
    try:
        # Read in the file
        with open(file_name, 'r') as file:
            filedata = file.read()
    
        # Replace the target string
        filedata = filedata.replace(file_search, file_replace)
    
        # Write the file out again
        with open(file_name, 'w') as file:
            file.write(filedata)
            return 0
    except OSError:
        print ("Could not open/read file:", file_name)
        return 1