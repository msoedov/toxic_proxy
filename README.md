# Toxic proxy

An asyncio tcp proxy for network resilience testing

```shell
pip install --upgrade  toxic_proxy
```

## Example

```python
import asyncio

from aiocassandra import aiosession
from cassandra.cluster import Cluster
from toxic_proxy import toxic_proxy

proxy = toxic_proxy(
    destination=('<cassandra-ip>', 9042), latency=5, port=9043)

cluster = Cluster('0.0.0.0:9043')
session = cluster.connect()
...
```

Simplified

```python
import asyncio
from toxic_proxy import toxic_proxy

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
```

Run the app and entry

```shell
curl -v 0.0.0.0:8888
```
