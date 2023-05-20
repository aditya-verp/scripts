import paramiko
import os

ssh = paramiko.SSHClient()

# path.expanduser(os.path.join) -> find the home/username path and joint with ~/.ssh/known_hosts
ssh.load_host_keys(os.path.expanduser(os.path.join("~",".ssh","known_hosts")))

# for ssh key use "key_filename=" and for password use "password= in ssh.connect"
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect("192.168.56.102",username="vagrant",password="vagrant")
sftp = ssh.open_sftp()
sftp.put("./test.py","/home/vagrant/newfile")

sftp.close() 
ssh.close() # Closed the open connection