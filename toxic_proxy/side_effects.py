import asyncio
import time
from collections import defaultdict

throttling = defaultdict(int)


async def latency(**opts):
    _latency = opts.get("latency")
    await asyncio.sleep(_latency or 0)


async def timeout(**opts):
    await asyncio.sleep(10 * 60 * 60)


async def bandwidth_rate_kb(**opts):
    throttling[int(time.time())] += 2
    sent = throttling[int(time.time())]
    _bandwidth_rate_kb = opts.get("bandwidth_rate_kb")
    if sent > _bandwidth_rate_kb:
        await asyncio.sleep(1)
