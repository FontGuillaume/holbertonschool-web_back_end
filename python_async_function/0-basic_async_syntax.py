#!/usr/bin/env python3
import random
import asyncio

# Coroutine asynchrone qui attend un délai aléatoire et le retourne
async def wait_random(max_delay: int = 10) -> float:
    # Génère un float aléatoire entre 0 et max_delay
    i = random.uniform(0, max_delay)
    # Attend pendant 'i' secondes de façon asynchrone
    await asyncio.sleep(i)
    # Retourne la valeur du délai
    return i
