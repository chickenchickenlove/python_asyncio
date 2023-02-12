import time
import asyncio
import inspect

async def main():
    for _ in range(10):
        await asyncio.sleep(1)
    return 'DONE'

coro = main()
loop = asyncio.get_event_loop()
loop.run_until_complete(coro)





