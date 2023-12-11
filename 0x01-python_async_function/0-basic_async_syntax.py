#!/usr/bin/env python3
"""
A module for asynchronous tasks using asyncio
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random amount of time up to `max_delay` seconds then
    returns the amount of time waited
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
