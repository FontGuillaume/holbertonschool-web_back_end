#!/usr/bin/env python3
"""
Ce script mesure le temps d'exécution de quatre
coroutines async_comprehension lancées en parallèle.
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine qui mesure le temps d'exécution pour lancer
    quatre async_comprehension en parallèle. Retourne le
    temps total écoulé en secondes.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time - start_time
