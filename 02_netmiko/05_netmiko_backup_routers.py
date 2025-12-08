from netmiko import ConnectHandler

with open('devices.txt') as f:
    devices = f.read().splitlines()

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
    connection = ConnectHandler(**cisco_device)
    print('Entering the enable mode...')

    if '>' in connection.find_prompt():
        connection.enable()
    #####################

    output = connection.send_command('show run')
    #print(output)

    prompt = connection.find_prompt()
    hostname = prompt[0:-1]
    #print(hostname)
    
    from datetime import datetime
    now = datetime.now()
    y = now.year
    m = now.month
    d = now.day
    
    filename = f'{hostname}_{y}-{m}-{d}.txt'
    with open(filename, 'w') as backup:
        backup.write(output)
        print(f'Backup of {hostname} completed successfully')
        print('#' * 30)


    ####### Disconnecting Device ##########
    print('Closing Connection')
    connection.disconnect()