#!/usr/bin/env python3
"""
Module qui fournit une fonction pour calculer la somme
d'une liste de nombres flottants.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calcule la somme des éléments d'une liste de nombres flottants.

    Args:
        input_list (List[float]): La liste des nombres à additionner.

    Returns:
        float: La somme de tous les éléments de la liste.
    """
    return sum(input_list)
