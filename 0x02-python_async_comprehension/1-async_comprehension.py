#!/usr/bin/env python3
"""
coroutine called async_comprehension that takes no arguments
"""
#import asyncio
#import async_generator
from typing import List
from importlib import import_module as using
async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collect 10 random numbers using an async comprehensing over async_generator
    Return:
    The 10 random numbers
    """
    return [num async for num in async_generator()]
