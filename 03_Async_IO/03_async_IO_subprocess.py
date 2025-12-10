import asyncio


async def run(cmd):
    proc = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    
    print(f'{cmd} exited with status code: {proc.returncode}')
    
    if stdout:
        print(f'STDOUT:\n{stdout.decode("UTF-8")}')
        
    if stderr:
        print(f'STDERR:\n{stderr.decode()}')

async def main(commands):
    tasks = []
    
    for cmd in commands:
        tasks.append(run(cmd))
    
    await asyncio.gather(*tasks)

commands = ('ipconfig', 'dir', 'route dir', 'arp -a', 'ping 8.8.8.8')

asyncio.run(main(commands))

