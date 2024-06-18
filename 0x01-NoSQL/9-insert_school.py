#!/usr/bin/env python3
""" 9-main """

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into the given MongoDB collection based on keyword arguments.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
