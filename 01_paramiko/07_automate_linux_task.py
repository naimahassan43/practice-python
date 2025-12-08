import myparamiko

client = myparamiko.connect('192.168.92.130', '22', 'admin', 'pass123')
shell = myparamiko.get_shell(client)

myparamiko.send_command(shell, 'uname -a')

cmd = 'sudo groupadd developers'
myparamiko.send_command(shell, cmd)
myparamiko.send_command(shell, 'pass123', 2)

myparamiko.show(shell)
myparamiko.send_command(shell, 'tail -n 1 /etc/group')


output = myparamiko.show(shell)
print(output)
myparamiko.close(client)