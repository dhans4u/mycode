#!/usr/bin/python3
"""Learning about Python SSH | rzfeeser@alta3.com"""

# paramiko does not come with standard library
# install with pip

import warnings
warnings.filterwarnings(action="ignore",module=".*paramiko.*")

import paramiko

sshsession = paramiko.SSHClient()

sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# if i need to SSH somewhere with a key, below is the code
mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

sshsession.connect(hostname="10.10.2.3", username="bender", pkey=mykey)

sshsession.exec_command("touch /home/bender/kissmyshineymetal.bender")

sessin, sessout, sesserr = sshsession.exec_command("ls /home/bender/")

print(sessout.read().decode('utf-8'))

sshsession.close()
