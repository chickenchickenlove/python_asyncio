import time
import asyncio

async def main():
    loop = asyncio.get_running_loop()

    future = loop.run_in_executor(None, blocking)
    asyncio.create_task(make_coro(future))

    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1)
    print(f'{time.ctime()} Good Bye!')


async def make_coro(future):
    try:
        return await future
    except asyncio.CancelledError:
        return await future


def blocking():
    time.sleep(1.5)
    print(f'{time.ctime()} Hello from a Thread!')

asyncio.run(main())