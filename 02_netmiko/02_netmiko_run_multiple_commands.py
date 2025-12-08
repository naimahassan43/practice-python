from netmiko import ConnectHandler
cisco_device = {
    'host':'192.168.92.11', 
    'port':'22', 
    'username':'admin', 
    'password':'admin', 
    'device_type':'cisco_ios', 
    'secret': 'cisco',         # this is enable password
    'verbose': True
    }
connection = ConnectHandler(**cisco_device)
print('Entering the enable mode...')

if '>' in connection.find_prompt():
    connection.enable()

# commands = ['int loopback 0', 'ip address 1.1.1.1 255.255.255.255', 'exit', 'username user2 secret cisco']
# output = connection.send_config_set(commands)
# cmd = 'ip ssh version 2;access-list 1 permit any;ip domain-name network-automation.io'
# output = connection.send_config_set(cmd.split(';'))
cmd = '''
ip ssh version 2
access-list 1 permit any
ip domain-name net-auto.io
'''
output = connection.send_config_set(cmd.split('\n'))

print(output)
print(connection.find_prompt())

#connection.send_command('write memory')

####### Disconnecting Device ##########
print('Closing Connection')
connection.disconnect()