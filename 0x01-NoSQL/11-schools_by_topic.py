#!/usr/bin/env python3
""" 10-main """

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    Retrieve a list of schools from the given MongoDB collection that have the specified topic.
    """
    return list(mongo_collection.find({'topics': topic}))
