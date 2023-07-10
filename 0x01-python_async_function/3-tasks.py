#!/usr/bin/env python3
"""
A non async function
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> float:
    """
    This is the main coroutine that creates
    and runs several subtasks in parallel.
    """
    return asyncio.create_task(wait_random(max_delay))
