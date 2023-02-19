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


def handler(sig):
    # loop = asyncio.get_running_loop()
    loop.stop()
    print(f'Got Signal: {sig!s}, shutting down')
    loop.remove_signal_handler(sig)
    loop.add_signal_handler(SIGINT, lambda: None)


if __name__ == '__main__':

    loop = asyncio.get_event_loop()

    for sig in (SIGINT, SIGTERM):
        loop.add_signal_handler(sig, handler, sig)

    task = loop.create_task(main())
    loop.run_forever()

    tasks = asyncio.all_tasks(loop=loop)
    for t in tasks:
        t.cancel()
    futures = asyncio.gather(*tasks, return_exceptions=True)
    loop.run_until_complete(futures)
    loop.close()