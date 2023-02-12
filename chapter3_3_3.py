import time
import asyncio
import inspect

async def func():
    print(f'coroutine started.')
    for i in range(5):
        await asyncio.sleep(1)
        print(f'sleep {i} sec')
    print(f'coroutine started.')
    return 123

async def main():
    ret = await func()
    return ret

c = main()

try:
    c.send(None)
except StopIteration as e:
    print(f'The answer was : {e.value}')




