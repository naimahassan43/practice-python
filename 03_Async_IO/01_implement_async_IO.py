import asyncio
import time

#Synchronous
def sync_f():
    print('one ', end='')
    time.sleep(1)
    print('two ', end='')
    
#ASynchronous
async def async_f():
    print('three ', end='')
    await asyncio.sleep(1)
    print('four ', end='')
    
async def main():
    #tasks = [async_f(), async_f(), asyncio]
    tasks = [async_f() for _ in range(3)]
        
    await asyncio.gather(*tasks)
start = time.time()
asyncio.run(main())    
end = time.time()

print(f'Execution time(Async): {end - start}')

print('\n') 
start = time.time()
for _ in range(3):
    sync_f()
end = time.time() 
print(f'Execution time(Sync): {end - start}')  
# async def f():
#     pass

# async def g():
#     await f()


