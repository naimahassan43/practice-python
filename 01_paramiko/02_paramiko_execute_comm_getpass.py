import paramiko
import time
import getpass

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

password = getpass.getpass('Enter Password:')
router = {'hostname':'192.168.92.11', 'port':'22', 'username':'admin', 'password':password}

print(f'Connecting to {router["hostname"]}')
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n')
shell.send('show version\n')
shell.send('show ip interface brief\n')
time.sleep(1)

output = shell.recv(10000)
#print(type(output))

output = output.decode('utf-8')
print(output)


if ssh_client.get_transport().is_active() == True:
    print('Closing Connection')
    ssh_client.close()