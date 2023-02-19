import time
import asyncio
from concurrent.futures import ThreadPoolExecutor as Executor


async def main():
    loop = asyncio.get_running_loop()
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1)
    print(f'{time.ctime()} Good Bye!')

def blocking():
    time.sleep(1.5)
    print(f'{time.ctime()} Hello from a Thread!')


loop = asyncio.get_event_loop()
executor = Executor()
loop.set_default_executor(executor)

task = loop.create_task(main())
future = loop.run_in_executor(None, blocking)
loop.run_until_complete(task)

pending = asyncio.all_tasks(loop=loop)
for t in pending: t.cancel()

loop.run_until_complete(asyncio.gather(*pending, return_exceptions=True))
executor.shutdown(wait=True)
loop.close()
