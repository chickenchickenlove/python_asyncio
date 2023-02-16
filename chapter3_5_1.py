import asyncio


async def main(f):
    await asyncio.sleep(1)
    f.set_result("hello")

future = asyncio.Future()
print(future.done())

loop = asyncio.get_event_loop()
coro = main(future)
task = loop.create_task(coro)
loop.run_until_complete(task)

print(future.done(), future.result())
















