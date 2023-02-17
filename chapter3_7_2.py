import asyncio
import aioredis

async def create_redis(h): pass
async def do_something_with(value): pass

async def main():
    redis = await create_redis(('localhost', 6379))
    keys = ['Americas', 'Africa', 'Europe', 'Asia']

    async for value in OneAtATime(keys):
        await do_something_with(value)

class OneAtATime:
    def __init__(self, redis, keys):
        self.redis = redis
        self.keys = keys
    def __aiter__(self):
        self.ikeys = iter(self.keys)
        return self
    async def __anext__(self):
        try:
            key = next(self.ikeys)
        except StopIteration:
            raise StopAsyncIteration

        value = await self.redis.get(key)
        return value

asyncio.run(main())