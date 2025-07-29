#!/usr/bin/env python3
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Exécute de façon concurrente n tâches
    task_wait_random avec un délai maximum donné,
    et retourne la liste des délais obtenus, dans l'ordre d'achèvement.

    Args:
        n (int): Nombre de tâches à lancer.
        max_delay (int): Délai maximum à passer à chaque tâche.

    Returns:
        list: Liste des délais retournés par
        chaque tâche, triés par ordre d'achèvement.
    """
    # Création de la liste des tâches à exécuter
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delay = await asyncio.gather(*tasks)
    return delay
