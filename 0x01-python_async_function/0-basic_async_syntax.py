#!/usr/bin/env python3
"""
    async function using type annonated
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ wait for a random amount of time
        and the return the amount of time waited

    """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
