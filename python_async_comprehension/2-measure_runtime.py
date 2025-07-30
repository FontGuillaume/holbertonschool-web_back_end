#!/usr/bin/env python3
"""
Ce script mesure le temps d'exécution de quatre
coroutines async_comprehension lancées en parallèle.
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension

"""
Coroutine qui mesure le temps d'exécution pour lancer
quatre async_comprehension en parallèle. Retourne le
temps total écoulé en secondes.
"""


async def measure_runtime() -> float:
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time
