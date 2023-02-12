import time
import asyncio
import inspect

async def for_coro():
    print(1)


async def main():
    loop = asyncio.get_event_loop()
    for _ in range(10):
        loop.create_task(for_coro())


async def main_after_get_running():
    # loop = asyncio.get_event_loop()
    for _ in range(10):
        asyncio.create_task(for_coro())

