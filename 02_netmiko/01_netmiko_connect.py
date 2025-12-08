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
output = connection.send_command('sh ip int brief')
print(output)

####### Disconnecting Device ##########
print('Closing Connection')
connection.disconnect()