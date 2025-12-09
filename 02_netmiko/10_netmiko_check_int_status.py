from netmiko import ConnectHandler

cisco_device = {
    'host':'192.168.92.12', 
    'port':'22', 
    'username':'admin', 
    'password':'admin', 
    'device_type':'cisco_ios', 
    'secret': 'admin', 
    'verbose': True
    }

connection = ConnectHandler(**cisco_device)

prompt = connection.find_prompt()

if '>' in prompt:
    connection.enable()

interface = input('Enter the interface you want to enable: ')
output = connection.send_command('sh ip interface ' + interface)
#print(output)

if 'Invalid input detected' in output:
    print('Please enter a valid interface')
else:
    first_line = output.splitlines()[0]
    print(first_line)
    if not 'up' in first_line:
        print('The interface is down. Enabling the interface ... ')
        commands = ['interface '+ interface, 'no shut', 'exit' ]
        output= connection.send_config_set(commands)
        print(output)
        print('#' * 40)
        print('The interface has been enabled')
    else:
        print('The interface ' + interface +  ' is already enabled')
connection.disconnect()