#!/usr/bin/env python3
"""
Module that
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """A function that measures an approximate elapsed time"""
    total_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - total_time)/n
