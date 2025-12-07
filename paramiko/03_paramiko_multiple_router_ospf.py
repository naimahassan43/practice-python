import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

router1 = {'hostname':'192.168.92.11', 'port':'22', 'username':'admin', 'password':'admin'}
router2 = {'hostname':'192.168.92.12', 'port':'22', 'username':'admin', 'password':'admin'}
router3 = {'hostname':'192.168.92.13', 'port':'22', 'username':'admin', 'password':'admin'}

routers = [router1, router2, router3]

for router in routers:
    print(f'Connecting to {router["hostname"]}')
    ssh_client.connect(**router, look_for_keys=False, allow_agent=False)

    shell = ssh_client.invoke_shell()

    shell.send('enable\n')
    shell.send('conf t\n')
    shell.send('router ospf 1\n')
    shell.send('network 0.0.0.0 0.0.0.0 area 0\n')
    shell.send('end\n')
    shell.send('terminal length 0\n')
    shell.send('show ip protocols\n')

    time.sleep(2)

    output = shell.recv(10000).decode()
    print(output)

########## closing connection #########
if ssh_client.get_transport().is_active() == True:
    print('Closing Connection')
    ssh_client.close()