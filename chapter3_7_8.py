import asyncio
from asyncio import StreamReader, StreamWriter

async def send_event(msg):
    await asyncio.sleep(100)
    pass

async def echo(reader: StreamReader, writer: StreamWriter):
    print('New connection')
    try:
        while data := await reader.readline():
            writer.write(data.upper())
            await writer.drain()
        print('Leaving Connection.')
    except asyncio.CancelledError:
        msg = 'Connection Closed'
        print(msg)
        await asyncio.create_task(send_event(msg))

        print('Connection dropped!')

async def main(host='127.0.0.1', port='8888'):
    server = await asyncio.start_server(echo, host, port)
    async with server:
        await server.serve_forever()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('Bye!')












