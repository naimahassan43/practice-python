from netmiko import ConnectHandler
linux = {
    'host':'192.168.92.130', 
    'port':'22', 
    'username':'admin', 
    'password':'pass123', 
    'device_type':'linux', 
    'secret': 'pass123',         # this is sudo password
    'verbose': True
    }
connection = ConnectHandler(**linux)
print('Entering the enable mode...')


connection.enable()
output = connection.send_command('apt update && apt install -y apache2')
#####################


####### Disconnecting Device ##########
print('Closing Connection')
connection.disconnect()