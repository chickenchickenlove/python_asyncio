import asyncio


# Signal 주는 것

async def main():
    while True:
        print(f'your application is running')
        await asyncio.sleep(1)

if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    task = loop.create_task(main())
    try:
        loop.run_until_complete(task)
    except KeyboardInterrupt:
        print('Got Signal: SIGINT, shutting down')

    tasks = asyncio.all_tasks(loop=loop)
    for t in tasks:
        t.cancel()
    futures = asyncio.gather(*tasks, return_exceptions=True)
    loop.run_until_complete(futures)
    loop.close()
