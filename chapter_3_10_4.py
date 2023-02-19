import asyncio
from signal import SIGTERM, SIGINT



async def main():

    try:
        while True:
            print(f'your application is running')
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        for i in range(3):
            print('<Your application is shutting down>')
            await asyncio.sleep(1)

if __name__ == '__main__':

    loop = asyncio.get_event_loop()

    task = loop.create_task(main())
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print('Got KeyboardInterrupt')

    tasks = asyncio.all_tasks(loop=loop)
    for t in tasks:
        t.cancel()
    futures = asyncio.gather(*tasks, return_exceptions=True)
    loop.run_until_complete(futures)
    loop.close()