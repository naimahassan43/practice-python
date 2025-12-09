from netmiko import ConnectHandler
from netmiko import file_transfer

cisco_device = {
    'host':'192.168.92.10', 
    'port':'22', 
    'username':'admin', 
    'password':'cisco', 
    'device_type':'cisco_ios', 
    'secret': 'cisco', 
    'verbose': True
    }

connection = ConnectHandler(**cisco_device)

transfer_output = file_transfer(
    connection, source_file='ospf.txt', 
    dest_file='ospf1.txt', 
    file_system='disk0:', 
    direction='put', 
    overwrite_file=True
    )

print(transfer_output)

connection.disconnect()