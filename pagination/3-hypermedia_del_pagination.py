#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retourne une page basée sur un index de départ donné.

        Cette méthode implémente une pagination résistante aux suppressions
        en utilisant les index originaux plutôt que des positions relatives.

        Args:
            index (int, optional): Index de départ pour la pagination.
                                Défaut: None
            page_size (int, optional): Nombre d'éléments par page.
                                      Défaut: 10

        Returns:
            Dict: Dictionnaire contenant :
                - index: Index de départ actuel
                - next_index: Index de départ pour la page suivante
                - page_size: Taille de page demandée
                - data: Données de la page actuelle

        Raises:
            AssertionError: Si l'index est hors des limites du dataset.
        """
        # Récupération du dataset pour validation des limites
        data = self.dataset()
        # Validation que l'index est dans les limites valides (0 <= index <
        # len)
        assert 0 <= index < len(data)
        # Récupération du dataset indexé pour accès par clé
        indexed_data = self.indexed_dataset()
        # Liste pour stocker les données de la page courante
        current_data = []
        # Calcul de l'index de départ pour la page suivante
        next_index = index + page_size

        # Parcours des index pour collecter les données de la page
        for i in range(index, next_index):
            # Vérification que l'index existe encore (non supprimé)
            if i in indexed_data:
                # Ajout de la ligne correspondante aux données courantes
                current_data.append(indexed_data[i])

        # Retour du dictionnaire avec toutes les informations de pagination
        return {
            'index': index,              # Index de départ de cette page
            'next_index': next_index,    # Index de départ page suivante
            'page_size': page_size,      # Taille de page demandée
            'data': current_data         # Données effectivement trouvées
        }
