#!/usr/bin/env python3
"""
Module qui fournit une fonction pour calculer
 la somme d'une liste contenant des entiers et des flottants.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calcule la somme des éléments d'une liste
      composée d'entiers et de flottants.

    Args:
        mxd_lst (List[Union[int, float]]): La liste des nombres
          à additionner (entiers ou flottants).

    Returns:
        float: La somme de tous les éléments de la
        liste, sous forme de flottant.
    """
    return sum(mxd_lst)
