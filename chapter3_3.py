import time
import asyncio
import inspect

async def func():
    return 123

c = func()

print(type(func))
print(f'func is coroutine? {inspect.iscoroutine(func)}')
print(f'func is coroutine function {inspect.iscoroutinefunction(func)}')
print(f'func() is coroutine? {inspect.iscoroutine(c)}')

