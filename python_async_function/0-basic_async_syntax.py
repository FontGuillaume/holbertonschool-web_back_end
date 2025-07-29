#!/usr/bin/env python3
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Attend un délai aléatoire et le retourne.
    """
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
