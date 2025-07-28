#!/usr/bin/env python3
"""
Module qui fournit une fonction pour créer un tuple
 à partir d'une chaîne et du carré d'un nombre.
"""

from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Crée un tuple contenant une chaîne
      et le carré d'un nombre (entier ou flottant).

    Args:
        k (str): La clé sous forme de chaîne de caractères.
        v (Union[int, float]): La valeur
        à élever au carré (entier ou flottant).

    Returns:
        Tuple[str, float]: Un tuple composé
          de la clé et du carré de la valeur (toujours en float).
    """
    return k, v * v
