
def file_text_insert(file_name,text_insert):
    try:
        # Read in the file
        with open(file_name, 'a') as file:
            file.write(text_insert)
            return 0
            
    except OSError:
        print ("Could not open/read file:", file_name)
        return 1