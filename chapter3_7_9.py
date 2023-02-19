import asyncio
from asyncio import StreamReader, StreamWriter

# 0으로 나눠서 문제가 되는 코드들

async def f(delay):
    await asyncio.sleep(1/delay)
    return delay


loop = asyncio.get_event_loop()
tasks = []
for delay in range(5):
    tasks.append(loop.create_task(f(delay)))
pendings = asyncio.all_tasks(loop=loop)
# loop.run_until_complete(tasks[1])

# for task in pendings:
#     task.cancel()
futures = asyncio.gather(*pendings, return_exceptions=True)
results = loop.run_until_complete(futures)
print(f'{results = }')
loop.close()