import time
import asyncio
import inspect

async def main():
    return 123

coro = main()
coro.throw(Exception, 'blah')



