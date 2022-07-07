#!/usr/bin/python3

from pipeline_url.task.tasks import url_access
import pymongo


client = pymongo.MongoClient()  # Creating mongo client

db = client["mydatabase"]

coll = db["links"]

if __name__ == "__main__":

    cursor = coll.find({})  # getting all links from collection

    for doc in cursor:
        url = doc["url"]
        url_access.apply_async(
            args=[url], queue="data_collection_queue"
        )  # calling function for each url
