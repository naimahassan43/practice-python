import asyncio
import asyncssh


async def connect_and_run(host, username, password, commands):
    async with asyncssh.connect(host=host, username=username, password=password, known_hosts=None) as connection:
        # result = await connection.run(command)
        # return result
        
        #### run multiple commands #######
        results = []
        for cmd in commands:
            result = await connection.run(cmd)
            results.append(result)
        
        return results
      
#command = 'ifconfig'
commands = ('ifconfig', 'who -a', 'uname -a', 'cat /etc/shadow')
#result = asyncio.run(connect_and_run('192.168.92.130', 'admin', 'pass123', command))
results = asyncio.run(connect_and_run('192.168.92.130', 'admin', 'pass123', commands))
for result in results:
    print(f'STDOUT:\n {result.stdout}')
    print(f'STDERR:\n {result.stderr}')
    print('#' * 50)