#!/usr/bin/env python3
"""
Cette fonction retourne la liste des écoles contenant un topic spécifique
 """


def schools_by_topic(mongo_collection, topic):
    """
    Avec une compréhension boucle et determine une condition
    pour ajouter topic dans school list
    """
    result = mongo_collection.find({"topics": topic})
    school_list = [
        document for document in result if topic in document.get(
            'topics', [])]
    return school_list
