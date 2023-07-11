#!/usr/bin/env python3
"""
A coroutine module
"""
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Function that uses async comprehension
    """
    result = [item async for item in async_generator()]
    return result
