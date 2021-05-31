import asyncio


@asyncio.coroutine
def tcp_echo_client(message, loop):
    reader, writer = yield from asyncio.open_connection('127.0.0.1', 9999, loop=loop)
    print('send :%r' % message)
    writer.write(message)
    data = yield from reader.read(100)
    print('received:%r' % data.decode())
    print('close socket')
    writer.close()


message = 'hellworld'
loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(message.encode(), loop))
loop.close()
