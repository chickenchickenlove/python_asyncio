import time
import asyncio
import inspect

async def func():
    print(f'coroutine started.')
    return 123

c = func()

try :
    c.send(None)
except StopIteration as e:
    print(f'The answer was : {e.value}')




