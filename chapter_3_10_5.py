import asyncio
from signal import SIGTERM, SIGINT


async def main():

    loop = asyncio.get_running_loop()
    for sig in (SIGINT, SIGTERM):
        loop.add_signal_handler(sig, handler, sig)

    try:
        while True:
            print(f'your application is running')
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        for i in range(3):
            print('<Your application is shutting down>')
            await asyncio.sleep(1)


def handler(sig):
    loop = asyncio.get_running_loop()
    pending = asyncio.all_tasks(loop=loop)
    for t in pending:
        t.cancel()
    print(f'Got Signal: {sig!s}, shutting down')
    loop.remove_signal_handler(sig)
    loop.add_signal_handler(SIGINT, lambda: None)


if __name__ == '__main__':
    asyncio.run(main())