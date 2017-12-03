import socket
import sideeffects
import asyncio

chunk_size = 2048

side_effects = {
    "latency": sideeffects.lattency,
    "timeout": sideeffects.timeout,
    "bandwidth_rate_kb": sideeffects.bandwidth_rate_kb,
}


def random_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", 0))
    s.listen(1)
    port = s.getsockname()[1]
    s.close()
    return port


async def toxic_proxy(destination,
                      latency: int=None,
                      timeout=None,
                      bandwidth_rate_kb: int=None,
                      slow_close=None,
                      port: int=None):
    if not port:
        port = random_port()
    opts = dict(
        latency=latency,
        timeout=timeout,
        bandwidth_rate_kb=bandwidth_rate_kb,
        slow_close=slow_close)

    async def handle_client(local_reader, local_writer):
        try:
            remote_reader, remote_writer = await asyncio.open_connection(
                *destination)
            upstream = _pipe(local_reader, remote_writer, **opts)
            downstream = _pipe(remote_reader, local_writer, **opts)
            await asyncio.gather(upstream, downstream)
        finally:
            local_writer.close()

    return await asyncio.start_server(handle_client, '0.0.0.0', port)


async def _pipe(reader, writer, **opts):
    try:
        while not reader.at_eof():
            for name, val in opts.items():
                sd = side_effects.get(name)
                if not sd or val is None:
                    continue
                print('Launching', name, val)
                await sd(**opts)
            writer.write(await reader.read(chunk_size))
    finally:
        writer.close()
