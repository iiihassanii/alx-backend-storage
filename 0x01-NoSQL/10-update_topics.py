#!/usr/bin/env python3
""" 10-main """

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    Python function that changes all topics of a school document based on the name
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
