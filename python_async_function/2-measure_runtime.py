#!/usr/bin/env python3
""" Mesure le temps moyen d'exécution de plusieurs coroutines asynchrones. """
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Mesure le temps moyen d'exécution de wait_n pour n coroutines.

    Args:
        n (int): Nombre de coroutines à lancer.
        max_delay (int): Délai maximum pour chaque coroutine.

    Returns:
        float: Temps moyen d'exécution par coroutine.
    """
    start = time.time()  # Démarre le chronomètre
    # Exécute les coroutines (doit être await si wait_n est async)
    wait_n(n, max_delay)
    end = time.time()  # Arrête le chronomètre
    # Calcule le temps moyen par coroutine
    return (end - start) % n
