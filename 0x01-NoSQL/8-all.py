#!/usr/bin/env python3
""" 8-main """

from pymongo import MongoClient


def list_all(mongo_collection):
    """
    List all documents in the given MongoDB collection.
    """
    all_documents = list(mongo_collection.find())
    return all_documents
