#!/usr/bin/env python3
"""
A coroutine module
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Function that uses async comprehension
    """
    result = [item async for item in async_generator()]
    return result
