import paramiko
from scp import SCPClient

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.connect (hostname='192.168.92.130', port=22, username='naima', password='674343',look_for_keys=False, allow_agent=False)

scp = SCPClient(ssh_client.get_transport())

#scp.put('devices.txt', '/tmp/aa.txt')
scp.put('devices.txt', '/tmp/aa.txt')
scp.close()