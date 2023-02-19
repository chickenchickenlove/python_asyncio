import asyncio
import aiohttp

async def main():
    urls = ['http://google.com', 'http://naver.com', 'http://daum.net', 'http://github.com']
    async with aiohttp.ClientSession() as session:
        responses = [response async for response in one_at_a_time(session, urls)]
        print(f'{responses=}')
    print('end job')

async def one_at_a_time(session, urls):
    for url in urls:
        yield await session.request('get', url)

asyncio.run(main())
