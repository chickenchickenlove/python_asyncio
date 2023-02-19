import asyncio
import aiohttp


async def f1(x):
    await asyncio.sleep(1)
    return x + 100

async def factory(n):
    for x in range(n):
        yield f1(x)


async def main():
    result = [await f async for f in factory(5)]
    print(f'{result=}')

asyncio.run(main())















