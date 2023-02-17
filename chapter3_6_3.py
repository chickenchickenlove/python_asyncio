from contextlib import asynccontextmanager

async def download_page(url): pass
async def update_stats(url): pass
def process(data): pass

@asynccontextmanager
async def web_page(url):
    data = await download_page(url)
    yield data
    await update_stats(url)

async with web_page('google.com') as data:
    process(data)
