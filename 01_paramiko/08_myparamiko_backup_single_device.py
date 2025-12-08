import myparamiko


router = {'server_ip':'192.168.92.11', 'server_port':'22', 'user':'admin', 'passwd':'admin'}     
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
#print(file_name)

with open(file_name, 'w') as f:
    f.write(output)
    
myparamiko.close(client)