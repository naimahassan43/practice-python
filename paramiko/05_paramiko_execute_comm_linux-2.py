import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

linux = {'hostname':'192.168.92.130', 'port':'22', 'username':'admin', 'password':'admin'}
print(f'Connecting to {linux["hostname"]}')
ssh_client.connect(**linux, look_for_keys=False, allow_agent=False)

stdin, stdout, stderr = ssh_client.exec_command('ifconfig\n')
output = stdout.read()
output = output.decode()
print(output)

stdin, stdout, stderr = ssh_client.exec_command('cat /etc/shadow\n')
time.sleep(0.5)
output = stdout.read()
output = output.decode()
print(output)

print(stderr.read().decode())
if ssh_client.get_transport().is_active() == True:
    print('Closing Connection')
    ssh_client.close()