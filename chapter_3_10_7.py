import time
import asyncio

async def main():
    loop = asyncio.get_running_loop()
    loop.run_in_executor(None, blocking)
    print(f'{time.ctime()} Hello!')
    await asyncio.sleep(1)
    print(f'{time.ctime()} Good Bye!')


def blocking():
    time.sleep(1.5)
    print(f'{time.ctime()} Hello from a Thread!')

asyncio.run(main())