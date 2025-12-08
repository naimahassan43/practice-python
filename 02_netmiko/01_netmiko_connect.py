# from netmiko import Netmiko

# connection = Netmiko(host='192.168.92.11', port='22', username='admin', password='admin',device_type='cisco_ios')

from netmiko import ConnectHandler

cisco_device = {
    'host':'192.168.92.11', 
    'port':'22', 
    'username':'admin', 
    'password':'admin', 
    'device_type':'cisco_ios', 
    'secret': 'cisco', 
    'verbose': True
    }

connection = ConnectHandler(**cisco_device)

prompt = connection.find_prompt()

if '>' in prompt:
    connection.enable()
    
output = connection.send_command('sh ip int br')
print(output)

if not connection. check_config_mode():
    connection.config_mode()
    
######### Enter global config mode####### 
#print(connection. check_config_mode())
connection.send_command('username user1 secret cisco')

######### Exit global config mode#######
connection.exit_config_mode()
print(connection. check_config_mode())
print(connection.send_command('sh run'))
####### Disconnecting Device ##########
print('Closing Connection')
connection.disconnect()