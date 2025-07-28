#!/usr/bin/env python3
"""
Module qui fournit une fonction pour créer
 un multiplicateur personnalisé sous forme de closure.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Crée une fonction qui multiplie
      un nombre flottant par un multiplicateur donné.

    Args:
        multiplier (float): Le multiplicateur
          à utiliser dans la fonction retournée.

    Returns:
        Callable[[float], float]: Une fonction qui prend un float en
          argument et retourne le produit de ce float par le multiplicateur.
    """
    def inner_fonction(x: float) -> float:
        """
        Multiplie l'argument x par le multiplicateur défini dans la closure.

        Args:
            x (float): Le nombre à multiplier.

        Returns:
            float: Le résultat de la multiplication.
        """
        return x * multiplier
    return inner_fonction
