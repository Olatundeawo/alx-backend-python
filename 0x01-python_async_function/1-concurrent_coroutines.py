#!/usr/bin/env python3
"""
    Import a function, spawn the function
    and return the list of all the delays
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    A function that import another function
    has two arguments and return a
    sorted lsit of the delays using the two arguments
    as a factor
    """
    time1 = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n))))
    return sorted(time1)
