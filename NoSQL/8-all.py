#!/usr/bin/env python3
def list_all(mongo_collection):
    """
    Liste tous les documents d'une collection MongoDB.

    Args:
        mongo_collection: objet collection pymongo.

    Returns:
        Liste de tous les documents, ou liste vide si aucun document.
    """
    result = mongo_collection.count_documents({})
    if result == 0:
        return []
    else:
        documents = list(mongo_collection.find())
        return documents
