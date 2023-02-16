import asyncio

async def my_coro():
    print('1')


coro = my_coro()
loop = asyncio.get_event_loop()

task1 = loop.create_task(coro)
assert isinstance(task1, asyncio.Task)

task2 = asyncio.ensure_future(coro)
assert isinstance(task2, asyncio.Task)

task3 = asyncio.ensure_future(task1)
assert task1 is task3












