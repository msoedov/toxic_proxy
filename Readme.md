# Toxic Proxy

Toxic Proxy is an asyncio-based TCP proxy designed for network resilience testing. This allows you to simulate network conditions like latency, bandwidth limitations, and other issues to test how your application behaves under different scenarios. Whether you're working with microservices or just need to test your network reliability, Toxic Proxy provides a flexible way to introduce network anomalies for better resilience testing.

## Features

- Simulate network latency
- Limit bandwidth
- Easy to integrate with Python applications
- Uses asyncio for high performance

## Installation

Install Toxic Proxy using pip.

```shell
pip install --upgrade toxic_proxy
```

## Quick Start

### Using with Cassandra

Here's an example that shows how to use Toxic Proxy with a Cassandra cluster.

```python
import asyncio
from aiocassandra import aiosession
from cassandra.cluster import Cluster
from toxic_proxy import toxic_proxy

# Create a proxy with latency
proxy = toxic_proxy(
    destination=('<cassandra-ip>', 9042),
    latency=5,
    port=9043
)

# Connect to Cassandra through the proxy
cluster = Cluster(['0.0.0.0:9043'])
session = cluster.connect()
# ... your code here ...


```

### Simplified Example

This example demonstrates a simple use case to limit bandwidth when connecting to google.com.

```python
import asyncio
from toxic_proxy import toxic_proxy

# Create a proxy with bandwidth limit
proxy = toxic_proxy(
    destination=('google.com', 80),
    bandwidth_rate_kb=0.5,
    port=8888
)

loop = asyncio.get_event_loop()
server = loop.run_until_complete(proxy)
print(f'Serving on {server.sockets[0].getsockname()}')

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()

```

### Testing

To test, you can use curl to make a request through the proxy.

```shell
curl -v 0.0.0.0:8888

```

## Contributing

We welcome contributions! If you find a bug or have a feature request, please open an issue. If you want to contribute code, feel free to open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
