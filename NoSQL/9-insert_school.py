#!/usr/bin/env python3
# Fonction pour insérer un document dans une collection MongoDB

def insert_school(mongo_collection, **kwargs):
    """
    Insère un nouveau document dans la collection MongoDB.

    Args:
        mongo_collection: objet collection pymongo.
        **kwargs: paires clé-valeur à insérer comme document.

    Returns:
        L'identifiant (_id) du document inséré.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
