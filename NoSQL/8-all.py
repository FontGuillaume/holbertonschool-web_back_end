#!/usr/bin/env python3
"""
that function list all documents on mongo_collection
"""


def list_all(mongo_collection):
    """
    Liste tous les documents d'une collection MongoDB.

    Args:
        mongo_collection: objet collection pymongo.

    Returns:
        Liste de tous les documents, ou liste vide si aucun document.
    """
    if mongo_collection is None:
        return []
    else:
        documents = (mongo_collection.find())
        return list(documents)
