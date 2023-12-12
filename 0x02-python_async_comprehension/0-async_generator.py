#!/usr/bin/env python3
"""
coroutine called async_generator that takes no arguments
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator function that yields a random float after every sec

    Returns:
        Generator: Asynchrous generator
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
