#!/usr/bin/env python3
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Exécute n tâches asynchrones avec un délai maximum
    et retourne la liste des délais obtenus.

    Args:
        n (int): Nombre de tâches à lancer.
        max_delay (int): Délai maximum pour chaque tâche.

    Returns:
        list: Liste des délais retournés par chaque tâche.
    """
    # Création de la liste des tâches à exécuter
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    # Exécution concurrente de toutes les tâches et récupération des résultats
    delay = await asyncio.gather(*tasks)
    # Retourne la liste des délais
    return delay
