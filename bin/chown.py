import os
import pwd

def chown(file,username):
    uid = pwd.getpwnam(username).pw_uid
    os.chown(file, uid, uid )