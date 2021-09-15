################################################################
#
# This python script is used to backup a WordPress configuration
# The MySQL Database
# And to send directories to another storage server
#
# Written by : Camille GASCHET
# Last change : September 5, 2021
# Tested with : Python 3.9.5
#
################################################################


# Imports list
import time
import os
import pipes
from ftplib import FTP
from ftplib import error_perm


# Displays python logo
def python_logo():
    logo = [
        "       __________          __   __                   ",
        "       \______   \___ __ _/  |_|  |__   ____   ____  ",
        "        |     ___<   |  |\   __\  |  \ /  _ \ /    \ ",
        "        |    |    \___  | |  | |   Y  (  <_> )   |  \ ",
        "        |____|    / ____| |__| |___|  /\____/|___|  /",
        "                  \/                \/            \/"
    ]
    for line in logo:
        print(line)


# Variables list for MySQL
MYSQL_BACKUP_PATH = '/backup'
MYSQL_NAME_TIME = time.strftime('MySQL_%d_%m_%Y_%H_%M_%S')
CREATE_MYSQL_BACKUP: str = MYSQL_BACKUP_PATH + '/' + MYSQL_NAME_TIME
DB_HOST = '192.168.1.100'
DB_USER = 'camcam'
DB_PASSWORD = 'password'
DB_NAME = 'wordpress'

# Variables list for WordPress
WORDPRESS_BACKUP_PATH = '/backup'
WORDPRESS_NAME_TIME = time.strftime('WordPress_%d_%m_%Y_%H_%M_%S')
CREATE_WORDPRESS_BACKUP: str = WORDPRESS_BACKUP_PATH + '/' + WORDPRESS_NAME_TIME

# Variables list for Apache
APACHE_BACKUP_PATH = '/backup'
APACHE_NAME_TIME = time.strftime('Apache_%d_%m_%Y_%H_%M_%S')
CREATE_APACHE_BACKUP: str = APACHE_BACKUP_PATH + '/' + APACHE_NAME_TIME

# Variables list for FTP
FTP_HOST = '192.168.1.200'
FTP_PORT = 21
FTP_USER = 'camcam'
FTP_PASSWORD = 'password'
FTP_SOURCE = r'/backup'


# Folder check for MySQL
def mysql_folder_check():
    """
    Check if the folder exists
    If not it is created
    :return:
    """
    try:
        print("[MySQL Backup] Checking directory...")
        os.stat(CREATE_MYSQL_BACKUP)
    except:
        print("[MySQL Backup] Adding directory...")
        os.mkdir(CREATE_MYSQL_BACKUP)
    pass


# Backup process for MySQL
def mysql_backup_process():
    """
    Creates the database backup
    Then it is compressed
    :return:
    """
    try:
        print("[MySQL Backup] Creating backup...")
        dump_command = 'mysqldump -h {0} -u {1} -p{2} {3} > {4}/{5}.sql'.format(DB_HOST,
                                                                                DB_USER,
                                                                                DB_PASSWORD,
                                                                                DB_NAME,
                                                                                pipes.quote(CREATE_MYSQL_BACKUP),
                                                                                DB_NAME)
        os.system(dump_command)
        print("[MySQL Backup] Compressing backup...")
        tar_command = 'tar -zcvf {0}.tar.gz {0}'.format(pipes.quote(CREATE_MYSQL_BACKUP))
        os.system(tar_command)
        rm_command = 'rm -drf /backup/*/'
        os.system(rm_command)
    except:
        print("[MySQL Backup] Operation failed...")
    pass


# Folder check for WordPress
def wordpress_folder_check():
    """
    Check if the folder exists
    If not it is created
    :return:
    """
    try:
        print("[WordPress Backup] Checking directory...")
        os.stat(CREATE_WORDPRESS_BACKUP)
    except:
        print("[WordPress Backup] Adding directory...")
        os.mkdir(CREATE_WORDPRESS_BACKUP)
    pass


# Backup process for WordPress
def wordpress_backup_process():
    """
    Creates the website backup
    Then it is compressed
    :return:
    """
    try:
        print("[WordPress Backup] Creating backup...")
        cp_command = 'cp -rp /var/www/wordpress/* {0}'.format(pipes.quote(CREATE_WORDPRESS_BACKUP))
        os.system(cp_command)
        print("[WordPress Backup] Compressing backup...")
        tar_command = 'tar -zcvf {0}.tar.gz {0}'.format(pipes.quote(CREATE_WORDPRESS_BACKUP))
        os.system(tar_command)
        rm_command = 'rm -drf /backup/*/'
        os.system(rm_command)
    except:
        print("[WordPress Backup] Operation failed...")
    pass


# Folder check for Apache
def apache_folder_check():
    """
    Check if the folder exists
    If not it is created
    :return:
    """
    try:
        print("[Apache Backup] Checking directory...")
        os.stat(CREATE_APACHE_BACKUP)
    except:
        print("[Apache Backup] Adding directory...")
        os.mkdir(CREATE_APACHE_BACKUP)
    pass


# Backup process for Apache
def apache_backup_process():
    """
    Creates the website backup
    Then it is compressed
    :return:
    """
    try:
        print("[Apache Backup] Creating backup...")
        cp_command = 'cp -rp /etc/apache2/* {0}'.format(pipes.quote(CREATE_APACHE_BACKUP))
        os.system(cp_command)
        print("[Apache Backup] Compressing backup...")
        tar_command = 'tar -zcvf {0}.tar.gz {0}'.format(pipes.quote(CREATE_APACHE_BACKUP))
        os.system(tar_command)
        rm_command = 'rm -drf /backup/*/'
        os.system(rm_command)
    except:
        print("[Apache Backup] Operation failed...")
    pass


# Copy on the remote server
def remote_copy():
    """
    Sends backups to the remote server
    Uses FTP
    :return:
    """
    try:
        print("[FTP] Connecting to the remote server...")
        ftp = FTP()
        ftp.connect(FTP_HOST, FTP_PORT)
        ftp.login(FTP_USER, FTP_PASSWORD)

        def files_copy(ftp_commands, path):
            for element in os.listdir(path):
                local_path = os.path.join(path, element)
                if os.path.isfile(local_path):
                    print("[FTP] Data accepted", element, local_path)
                    ftp_commands.storbinary('STOR ' + element, open(local_path, 'rb'))
                elif os.path.isdir(local_path):
                    print("[FTP] Directory created", element)
                    try:
                        ftp_commands.mkd(element)
                    except error_perm as e:
                        value_args = e.args[0]
                        if not value_args.startswith('550'):
                            raise
                    print("[FTP] Directory changed", element)
                    ftp_commands.cwd(element)
                    files_copy(ftp_commands, local_path)
                    print("[FTP] Directory changed", "..")
                    ftp_commands.cwd("..")

        ftp.cwd('/backup')
        files_copy(ftp, FTP_SOURCE)
        ftp.quit()
    except:
        print("[FTP] Unable to connect to the remote server...")
    pass


# Main function
def main():
    """
    Performs the various functions
    :return:
    """
    try:
        python_logo()
        mysql_folder_check()
        mysql_backup_process()
        wordpress_folder_check()
        wordpress_backup_process()
        apache_folder_check()
        apache_backup_process()
        remote_copy()
    except:
        print("[MySQL Backup] ERROR - Unable to backup")
        print("[WordPress Backup] ERROR - Unable to backup")
        print("[Apache Backup] ERROR - Unable to backup")
    pass


# Run the main program
if __name__ == '__main__':
    main()
