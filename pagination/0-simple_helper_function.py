#!/usr/bin/env python3
"""
Module contenant une fonction helper pour la pagination.
Ce module fournit des utilitaires pour calculer les indices
de début et de fin pour une page donnée dans un système de pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calcule les indices de début et de fin pour une page donnée.
    
    Cette fonction prend un numéro de page et une taille de page,
    puis retourne un tuple contenant l'indice de début (inclus)
    et l'indice de fin (exclus) pour cette page.
    
    Args:
        page (int): Le numéro de la page (commence à 1)
        page_size (int): Le nombre d'éléments par page
        
    Returns:
        tuple: Un tuple (start_index, end_index) où:
            - start_index: Premier indice de la page (inclus)
            - end_index: Dernier indice + 1 de la page (exclus)
            
    Examples:
        >>> index_range(1, 7)
        (0, 7)
        >>> index_range(3, 15)
        (30, 45)
    """
    # Calcul de l'indice de début
    # On soustrait 1 car les pages commencent à 1 mais les indices à 0
    start_index = (page - 1) * page_size
    
    # Calcul de l'indice de fin (exclusif)
    # C'est le premier indice de la page suivante
    end_index = start_index + page_size
    
    # Retourne un tuple contenant les deux indices
    return (start_index, end_index)