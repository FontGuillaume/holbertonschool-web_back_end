#!/usr/bin/env python3
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Exécute de façon concurrente n coroutines
    wait_random avec un délai maximum donné,
    et retourne la liste des délais obtenus, dans l'ordre d'achèvement.

    Args:
        n (int): Nombre de coroutines à lancer.
        max_delay (int): Délai maximum à passer à chaque coroutine.

    Returns:
        list: Liste des délais retournés par
        chaque coroutine, triés par ordre d'achèvement.
    """
    # Création de la liste des coroutines à exécuter
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = []
    # Parcours des coroutines au fur et à mesure qu'elles se terminent
    for tasks in asyncio.as_completed(tasks):
        results.append(await tasks)
    return results
