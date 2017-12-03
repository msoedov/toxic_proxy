import time
from collections import defaultdict
import asyncio

trottling = defaultdict(int)


async def lattency(**opts):
    _latency = opts.get("latency")
    await asyncio.sleep(_latency or 0)


async def timeout(**opts):
    await asyncio.sleep(10 * 60 * 60)


async def bandwidth_rate_kb(**opts):
    trottling[int(time.time())] += 2
    sent = trottling[int(time.time())]
    _bandwidth_rate_kb = opts.get("bandwidth_rate_kb")
    if sent > _bandwidth_rate_kb:
        await asyncio.sleep(1)
