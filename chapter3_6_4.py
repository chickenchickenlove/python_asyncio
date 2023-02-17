import asyncio
from contextlib import asynccontextmanager

def download_page(url): pass
def update_stats(url): pass
def process(data): pass

@asynccontextmanager
async def web_page(url):
    loop = asyncio.get_running_loop()
    data = await loop.run_in_executor(None, download_page, url)
    yield data
    await loop.run_in_executor(None, update_stats, url)

async with web_page('google.com') as data:
    process(data)
