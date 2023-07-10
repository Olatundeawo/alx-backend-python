#!/usr/bin/env python3
"""
Using async function
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    A function that import another function
    has two arguments and return a
    sorted lsit of the delays using the two arguments
    as a factor
    """
    time1 = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n))))
    return sorted(time1)
