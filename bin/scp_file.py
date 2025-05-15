import os

def scp_file(file,pass_file,user,host,remote_dir,local_dir):
    output = os.system("sshpass -f " + pass_file + " scp " + user + "@" + host + ":" + remote_dir + file + " " + local_dir)
    return output