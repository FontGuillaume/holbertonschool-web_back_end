#!/usr/bin/env python3
"""
Module d’exemple pour les annotations de type.
Ce module contient une fonction qui concatène deux chaînes de caractères.
"""


def concat(str1: str, str2: str) -> str:
    """
    Concatène deux chaînes de caractères et retourne le résultat.

    Args:
        str1 (str): La première chaîne à concaténer.
        str2 (str): La seconde chaîne à concaténer.

    Returns:
        str: La chaîne résultant de la concaténation de str1 et str2.
    """
    return str1 + str2
