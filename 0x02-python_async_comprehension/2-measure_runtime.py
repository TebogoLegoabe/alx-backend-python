#!/usr/bin/env python3
"""
measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather
"""
import asyncio
import time
from importlib import import_module as using

async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Asynchronous function that measures and returns the runtime of
    running 4 instances of the async_comprehension function
    Returns:
        float: The runtime of the async_comprehension
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
