#!/usr/bin/env python3
"""
A coroutine program
"""
import asyncio
import random


async def async_generator():
    """
    A function that loop 10 times, each time
    asynchronously wait 1 second,
    then yield a random number between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)

        yield random.uniform(0, 10)
