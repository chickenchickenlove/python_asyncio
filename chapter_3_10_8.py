import time
import asyncio

async def main():
    loop = asyncio.get_running_loop()
    future = loop.run_in_executor(None, blocking)
    try:
        print(f'{time.ctime()} Hello!')
        await asyncio.sleep(1)
        print(f'{time.ctime()} Good Bye!')
    finally:
        await future  ## 종료될 때까지 대기


def blocking():
    time.sleep(1.5)
    print(f'{time.ctime()} Hello from a Thread!')

asyncio.run(main())