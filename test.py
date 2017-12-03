import asyncio
from app import toxic_proxy

proxy = toxic_proxy(
    destination=('google.com', 80), bandwidth_rate_kb=0.5, port=8888)
loop = asyncio.get_event_loop()

server = loop.run_until_complete(proxy)
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
