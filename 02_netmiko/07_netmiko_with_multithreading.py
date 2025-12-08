from netmiko import ConnectHandler
import time
import threading

start = time.time()

def backup(device):
    connection = ConnectHandler(**device)
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


with open('devices.txt') as f:
    devices = f.read().splitlines()

threads = list()
for ip in devices:
    device = {
        'host': ip, 
        'port':'22', 
        'username':'admin', 
        'password':'admin', 
        'device_type':'cisco_ios', 
        'secret': 'cisco',         # this is enable password
        'verbose': True
        }
    th = threading.Thread(target=backup, args=(device, ))
    threads.append(th)

for th in threads:
    th.start()
    
for th in threads:
    th.join()
    
end = time.time()
print(f'Total execution time:{end-start}')