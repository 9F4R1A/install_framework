import configparser
import sys
import pre_install

from bin.file_text_insert import file_text_insert

config = configparser.ConfigParser()
config.sections()
config.read('conf/install.cfg')

logfile = config['generic']['logfile']

file_text_insert(logfile,"\n")
file_text_insert(logfile,"LOGO\n")
file_text_insert(logfile, "\n")

file_text_insert(logfile,"\n------------------------\n --- hostname --- \n------------------------\n")
print(" --- hostname --- ")
ch = pre_install.config_hostname()
print()
if ch == 0:
    file_text_insert(logfile,"\n------------------------\n --- timezone --- \n------------------------\n")
    print(" --- timezone --- ")
    cct = pre_install.check_config_timezone()
    print()
    if cct == 0:
        file_text_insert(logfile,"\n------------------------\n --- selinux --- \n------------------------\n")
        print(" --- selinux --- ")
        ccs = pre_install.check_config_selinux()
        print()
        if ccs == 0:
            file_text_insert(logfile,"\n------------------------\n --- repos --- \n------------------------\n")
            print(" --- repos --- ")
            cir = pre_install.check_install_repo()
            print()
            if cir == 0:
                file_text_insert(logfile,"\n------------------------\n --- packages --- \n------------------------\n")
                print(" --- packages --- ")
                cip = pre_install.check_install_packages()
                print()
                if cip == 0:
                    file_text_insert(logfile,"\n------------------------\n --- ports tcp --- \n------------------------\n")
                    print(" --- ports --- ")
                    cfp_tcp = pre_install.check_fw_ports("tcp")
                    print()
                    if cfp_tcp == 0:
                        file_text_insert(logfile,"\n------------------------\n --- ports udp --- \n------------------------\n")
                        cfp_udp = pre_install.check_fw_ports("udp")
                        print()
                        if cfp_udp == 0:
                            file_text_insert(logfile,"\n------------------------\n --- create known hosts --- \n------------------------\n")
                            print(" --- create known hosts --- ")
                            cckh = pre_install.call_check_known_hosts()
                            print()
                            if cckh == 0:
                                file_text_insert(logfile,"\n------------------------\n --- install finished with success --- \n------------------------\n")
                                print(" --- install finished with success --- ")
                            else:
                                file_text_insert(logfile,"\n --- Error config known hosts --- ")
                                sys.exit("Error config known hosts")
                        else:
                            file_text_insert(logfile,"\n --- Error config udp ports --- ")
                            sys.exit("Error config udp ports")
                    else:
                        file_text_insert(logfile,"\n --- Error config tcp ports --- ")
                        sys.exit("Error config tcp ports")
                else:
                    file_text_insert(logfile,"\n --- Error install packages --- ")
                    sys.exit("Error install packages")
            else:
                file_text_insert(logfile,"\n --- Error install repos --- ")
                sys.exit("Error install repos")
        else:
            file_text_insert(logfile,"\n --- Error setting selinux --- ")
            sys.exit("Error setting selinux")
    else:
        file_text_insert(logfile,"\n --- Error setting timezone --- ")
        sys.exit("Error setting timezone")
else:
    file_text_insert(logfile,"\n --- Error setting hostname --- ")
    sys.exit("Error setting hostname")


















