#!/usr/bin/env python3
"""
Module qui fournit une fonction pour
 associer à chaque élément d'un itérable sa longueur.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Retourne une liste de tuples
      contenant chaque élément de l'itérable et sa longueur.

    Args:
        lst (Iterable[Sequence]): Un itérable d'objets
          séquences (ex: str, list, tuple).

    Returns:
        List[Tuple[Sequence, int]]: Liste de
          tuples (élément, longueur de l'élément).
    """
    return [(i, len(i)) for i in lst]
