import time
import asyncio


async def main(wait_time):
    for i in range(wait_time):
        print(f'coroutine wait {i} sec. \n')
        await asyncio.sleep(1)

    print(f'coroutine completed.')

def blocking(wait_time):
    for i in range(wait_time):
        print(f'blocking wait {i} sec \n')
        time.sleep(1)

    print(f'blocking func completed')


loop = asyncio.get_event_loop()
task = loop.create_task(main(3))
loop.run_in_executor(None, blocking, 2)
loop.run_until_complete(task)
pending = asyncio.all_tasks(loop=loop)

for task in pending:
    task.cancel()

group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()



