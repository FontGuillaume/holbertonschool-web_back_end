#!/usr/bin/env python3
""" Lance plusieurs coroutines asynchrones et
retourne leurs délais d'exécution. """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Exécute n coroutines wait_random avec un délai maximum
    et retourne la liste des délais obtenus, dans l'ordre d'achèvement.

    Args:
        n (int): Nombre de coroutines à lancer.
        max_delay (int): Délai maximum à passer à chaque coroutine.

    Returns:
        list: Liste des délais retournés par
        chaque coroutine, triés par ordre d'achèvement.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delay = [await tasks for tasks in asyncio.as_completed(tasks)]
    return delay
