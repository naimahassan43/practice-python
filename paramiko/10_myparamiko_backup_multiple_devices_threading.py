import myparamiko
import threading

def backup(router):
    client = myparamiko.connect(**router)
    shell = myparamiko.get_shell(client)

    myparamiko.send_command(shell, 'terminal length 0')
    myparamiko.send_command(shell, 'show run')

    output = myparamiko.show(shell)


    output_list = output.splitlines()
    output_list = output_list[9:-1]
    #print(output_list)
    output = '\n'.join(output_list)
    #print(output)

    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    file_name = f'{router["server_ip"]}_{year}-{month}-{day}.txt'

    with open(file_name, 'w') as f:
        f.write(output)
    
    myparamiko.close(client)
    
    
router1 = {'server_ip':'192.168.92.11', 'server_port':'22', 'user':'admin', 'passwd':'admin'}     
router2 = {'server_ip':'192.168.92.12', 'server_port':'22', 'user':'admin', 'passwd':'admin'}     
router3 = {'server_ip':'192.168.92.13', 'server_port':'22', 'user':'admin', 'passwd':'admin'}  

routers = [router1, router2, router3]

threads = list()
for router in routers:
    th = threading.Thread(target=backup, args=(router,))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()