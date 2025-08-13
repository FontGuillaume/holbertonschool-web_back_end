#!/usr/bin/env python3
def list_all(mongo_collection):
    result = mongo_collection.count_documents({})
    if result == 0:
        return []
    else:
        documents = list(mongo_collection.find())
        return documents
    