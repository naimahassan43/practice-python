from netmiko import ConnectHandler
with open('devices.txt') as f:
    devices = f.read().splitlines()

device_list = list()

for ip in devices:
    cisco_device = {
        'host': ip, 
        'port':'22', 
        'username':'admin', 
        'password':'admin', 
        'device_type':'cisco_ios', 
        'secret': 'cisco',         # this is enable password
        'verbose': True
        }
    device_list.append(cisco_device)

#print(device_list)
#exit(1)

for device in device_list:
    connection = ConnectHandler(**device)
    print('Entering the enable mode...')

    if '>' in connection.find_prompt():
        connection.enable()
    #####################
    file = input(f'Enter a configuration file (use a valid path) for {device["host"]}: ')
    
    print(f'Running commands from file: {file} on device: {device["host"]}')
    output = connection.send_config_from_file(file)
    print(output)

    ####### Disconnecting Device ##########
    print(f'Closing Connection to {cisco_device["host"]}')
    connection.disconnect()
    
    print('#' * 30)