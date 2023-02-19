import asyncio
import aiohttp


async def f(delay):
    await asyncio.sleep(delay)

loop = asyncio.get_event_loop()
t1 = loop.create_task(f(1))
t2 = loop.create_task(f(2))
loop.run_until_complete(t1)

# 종료 로직
tasks = asyncio.all_tasks(loop=loop)
for t in tasks:
    t.cancel()
futures = asyncio.gather(*tasks, return_exceptions=True)
loop.run_until_complete(futures)
#  종료 로직

loop.close()




