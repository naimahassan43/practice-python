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
#####################
print('Send commands from file')
output = connection.send_config_from_file('ospf.txt')
print(output)

####### Disconnecting Device ##########
print('Closing Connection')
connection.disconnect()