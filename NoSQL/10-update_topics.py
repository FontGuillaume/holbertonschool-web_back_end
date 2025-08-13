#!/usr/bin/env python3
"""
Fonction pour mettre à jour les topics d'une école selon son nom.
"""


def update_topics(mongo_collection, name, topics):
    """
    Met à jour tous les documents dont le nom correspond à 'name' en
    remplaçant la liste des topics par 'topics'.

    Args:
        mongo_collection: objet collection pymongo.
        name: nom de l'école à mettre à jour (str).
        topics: nouvelle liste de topics (list de str).
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
