import configparser
import sys
from tqdm import tqdm
from bin.add_repo import add_repo
from bin.check_fw import check_fw
from bin.check_package import check_package
from bin.install_package import install_package
from bin.add_fw_port import add_fw_port
from bin.check_repo import check_repo
from bin.check_selinux import check_selinux
from bin.set_selinux import set_selinux
from bin.check_timezone import check_timezone
from bin.set_timezone import set_timezone
from bin.check_file import check_file
from bin.set_hostname import set_hostname
from bin.file_text_insert import file_text_insert
from bin.create_known_hosts import create_known_hosts

config = configparser.ConfigParser()
config.sections()
config.read('conf/install.cfg')
logfile = config['generic']['logfile']

def config_hostname():
    with tqdm(total=100) as pbar:
        hostname = config['generic']['hostname']
        ipaddress = config['generic']['ipaddress']
        #check hostname first
        conf_hostname = set_hostname(hostname,ipaddress)
        pbar.update(20)
        if conf_hostname == 0:
            file_text_insert(logfile,"\nHostname was set to" + hostname)
            pbar.update(80)
            return 0
        else:
            sys.exit("Error setting Hostname")


def check_config_timezone():
    with tqdm(total=100) as pbar:
        config_timezone = check_timezone()
        pbar.update(20)
        if config_timezone == 0:
            file_text_insert(logfile,"\nTimezone already set to UTC")
            pbar.update(80)
            return 0
        elif config_timezone == 1:
            set_config_timezone = set_timezone()
            pbar.update(20)
            if set_config_timezone == 0:
                file_text_insert(logfile,"\nTimezone was set to UTC")
                pbar.update(60)
                return 0
            else:
                sys.exit("Error setting Timezone to UTC")


def check_config_selinux():
    with tqdm(total=100) as pbar:
        config_selinux = check_selinux()
        pbar.update(20)
        if config_selinux == 0:
            file_text_insert(logfile,"\nSelinux already set to Permissive")
            pbar.update(80)
            return 0
        elif config_selinux == 1:
            set_config_selinux = set_selinux()
            if set_config_selinux == 0:
                file_text_insert(logfile,"\nSelinux was set to Permissive")
                pbar.update(80)
                return 0
            else:
                sys.exit("Error setting Selinux to permissive")


def check_install_repo():
    repos = config['prechecks']['repos']
    repo = repos.split()
    repo_total = len(repo)
    bar_segment = 100 / repo_total
    with tqdm(total=100) as pbar:
        for each_repo in repo:
            installed_repo = check_repo(each_repo)
            if installed_repo == 0:
                file_text_insert(logfile,"\nrepo " + each_repo + " is installed\n")
            elif installed_repo == 1:
                file_text_insert(logfile,"\nrepo " + each_repo + " needs installation\n" )
                inst_result_repo = add_repo(each_repo)
                if inst_result_repo == 0:
                    file_text_insert(logfile,"\nrepo " + each_repo + " was installed\n-----------\n")
                else:
                    file_text_insert(logfile,"\nerror installing repo: " + each_repo)
            pbar.update(bar_segment)
        return 0


def check_install_packages():    
    packages = config['prechecks']['package_list']
    package = packages.split()
    pack_total = len(package)
    bar_segment = 100 / pack_total
    with tqdm(total=100) as pbar:
        for each_package in package:
            installed_package = check_package(each_package)
            if installed_package == 0:
                file_text_insert(logfile,"\npackage " + each_package + " is installed\n-----------\n")
            elif installed_package == 1:
                file_text_insert(logfile,"\npackage " + each_package + " needs installation\n")    
                inst_result_package = install_package(each_package)
                if inst_result_package == 0:
                    file_text_insert(logfile,"\npackage " + each_package + " was installed\n-----------\n")
                else:
                    file_text_insert(logfile,"\nerror installing package: " + each_package )
            pbar.update(bar_segment)
        return 0


def check_fw_ports(nt_type):
    ports = config['prechecks']['ports_'+ nt_type]
    port = ports.split()
    port_total = len(port)
    bar_segment = 100 / port_total
    with tqdm(total=100) as pbar:
        if nt_type == "tcp":
            pbar.update(0.00000000000006)
        for each_port in port:
            configured_port = check_fw(each_port)
            if configured_port == 0:
                file_text_insert(logfile,"\nport " + nt_type+ " " + each_port + " is configured\n")
            elif configured_port == 1:
                file_text_insert(logfile,"\nport " + nt_type+ " " + each_port + " needs to be configured\n")
                conf_result_port = add_fw_port(each_port,nt_type)
                if conf_result_port == 0:
                    file_text_insert(logfile,"\nport " + nt_type+ " " + each_port + " was configured\n-----------\n")
                else:
                    file_text_insert(logfile,"\nError configuring port: " + nt_type+ " " + each_port )
            pbar.update(bar_segment)
        return 0


def call_check_known_hosts():
    with tqdm(total=100) as pbar:
        out_check_known_hosts = check_file("/root/.ssh/known_hosts","") #known host you need to check
        pbar.update(20)
        if out_check_known_hosts == 0:
            file_text_insert(logfile,"\nknown_hosts already created")
            pbar.update(80)
            return 0
        elif out_check_known_hosts == 1:
            create_known_hosts()
            file_text_insert(logfile,"\nknown_hosts was created")
            pbar.update(80)
            return 0
        else:
            file_text_insert(logfile,"\nError creating known_hosts")
            return 1
