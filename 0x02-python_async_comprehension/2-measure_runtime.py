#!/usr/bin/env python3
"""
coroutine moodule
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    A function that measure the runtime
    it was roughly 10 seconds because the
    range was set the 10
    """
    s = time.perf_counter()
    await asyncio.gather(
        async_comprehension(), async_comprehension(),
        async_comprehension(),
        async_comprehension())
    total = time.perf_counter() - s
    return total
