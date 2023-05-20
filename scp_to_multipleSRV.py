import paramiko
import os

hostfile_path = input("Enter the host file Path: ")
host_list = []
host_list_len = len(host_list)
with open('demo.txt', 'r') as f:
    host_list = [line.strip() for line in f]

ssh = paramiko.SSHClient()
# path.expanduser(os.path.join) -> find the home/username path and joint with ~/.ssh/known_hosts
ssh.load_host_keys(os.path.expanduser(os.path.join("~",".ssh","known_hosts")))
check = input("Choose the Connection method ('pswd' O:)R 'key'): ")

if check == "pswd":
    u,p = input("Enter the Username ,Password in the order (seprated by SPACE): ").split()
    local_path,remote_path = input("Enter the local path fist and inthe second remote path (seperated by SPACE): ").split()
    for i in range(len(host_list)):
        hs = host_list[i]
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect((hs),username=(u),password=(p))
        sftp = ssh.open_sftp()
        sftp.put((local_path),(remote_path))
    print("\n")
    print("##### Success #####")
   
elif check == "key":
    u,p = input("Enter the Username , Password in the order (seprated by SPACE): ").split()
    key_filename = input("Enter the ssh key file path: ")
    local_path,remote_path = input("Enter the local path fist and inthe second remote path (seperated by SPACE): ").split()
    for i in range(len(host_list)):
        hs = host_list[i]
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect((hs),username=(u),key_filename=(key_filename))
        sftp = ssh.open_sftp()
        sftp.put((local_path),(remote_path))
    print("\n")
    print("##### Success #####")
else:
    print("Please enter the right input")

sftp.close() 
ssh.close() # Closed the open connection