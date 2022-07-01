#!/usr/bin/python3

from __future__ import absolute_import
from pipeline_url.celery.celeryapp import app
import json
import pymongo
import requests


@app.task
def url_access(url):
    print(url)
    r = requests.get(url)

    d = json.loads(r.text)  # Converting string to dictionary

    items = d["result"]["items"]  # Getting dictionary of all items

    client = pymongo.MongoClient()

    mydb = client["mydatabase"]

    mycol = mydb["urls"]

    for item in items:
        mycol.insert_one(item)  # Inserting each item in collection

    print("Successfully added to database.")


# add "url_access" task to the beat schedule
