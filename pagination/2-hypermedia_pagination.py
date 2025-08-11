#!/usr/bin/env python3
"""
Module de pagination simple pour une base
de données de noms de bébés populaires.

Ce module implémente une classe Server qui permet de paginer efficacement
un dataset CSV en utilisant la fonction helper index_range.
"""
import csv
import math
from typing import List

# Import de la fonction helper pour calculer les indices de pagination
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """
    Classe Server pour paginer une base de données de noms de bébés populaires.

    Cette classe charge un fichier CSV contenant des données de noms de bébés
    et fournit des méthodes pour accéder aux données de manière paginée.

    Attributes:
        DATA_FILE (str): Chemin vers le fichier CSV contenant les données
        __dataset (List[List] | None): Cache privé pour stocker le dataset
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialise une nouvelle instance de Server.

        Le dataset n'est pas chargé immédiatement mais sera mis en cache
        lors du premier accès via la méthode dataset().
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Retourne le dataset mis en cache.

        Cette méthode implémente un pattern de lazy loading : les données
        ne sont chargées qu'au premier appel et mises en cache pour les
        appels suivants.

        Returns:
            List[List]: Dataset sans la ligne d'en-tête, chaque ligne
                       étant une liste de chaînes de caractères.

        Note:
            La première ligne (en-têtes) est automatiquement supprimée
            du dataset retourné.
        """
        if self.__dataset is None:
            # Ouverture et lecture du fichier CSV
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                # Conversion de toutes les lignes en liste
                dataset = [row for row in reader]
            # Suppression de la ligne d'en-tête (index 0)
            # et stockage dans le cache privé
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retourne une page spécifique du dataset.

        Cette méthode utilise la fonction index_range pour calculer les indices
        appropriés et retourne la portion correspondante du dataset.

        Args:
            page (int, optional): Numéro de la page à récupérer (commence à 1).
                                 Défaut: 1
            page_size (int, optional): Nombre d'éléments par page.
                                      Défaut: 10

        Returns:
            List[List]: Liste des lignes pour la page demandée.
                       Retourne une liste vide si la page est hors limites.

        Raises:
            AssertionError: Si page ou page_size ne sont
            pas des entiers positifs.

        Examples:
            >>> server = Server()
            >>> server.get_page(1, 5)  # Première page, 5 éléments
            >>> server.get_page(2)     # Deuxième page, 10 éléments (défaut)
        """
        # Validation des paramètres d'entrée
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Récupération du dataset complet
        data = self.dataset()

        # Calcul des indices de début et de fin pour la page demandée
        start_index, end_index = index_range(page, page_size)

        # Vérification que la page demandée existe dans le dataset
        # Si l'index de début est valide, on retourne la tranche
        if start_index < len(data) or end_index > len(data):
            return data[start_index:end_index]

        # Retourne une liste vide si la page est hors limites
        return []
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        data = self.dataset()
        current_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(data) / page_size)
        if page < total_pages:
            next_page = page + 1
        else:
            next_page = None

        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None

        return {
            'page_size': page_size,
            'page': page,
            'data': current_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }





