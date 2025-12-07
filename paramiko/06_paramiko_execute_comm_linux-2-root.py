import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

linux = {'hostname':'192.168.92.130', 'port':'22', 'username':'admin', 'password':'admin'}
print(f'Connecting to {linux["hostname"]}')
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh_client.exec_command('sudo useradd user1\n', get_pty=True)
stdin.write('adminPass\n')
time.sleep(2)

stdin, stdout, stderr = ssh_client.exec_command('cat /etc/shadow\n')
print(stderr.read().decode())
time.sleep(1)

if ssh_client.get_transport().is_active() == True:
    print('Closing Connection')
    ssh_client.close()