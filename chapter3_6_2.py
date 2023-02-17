from contextlib import contextmanager

def download_page(url): pass
def update_stats(url): pass
def process(data): pass

@contextmanager
def web_page(url):
    data = download_page(url)
    yield data
    update_stats(url)

with web_page('google.com') as data:
    process(data)
