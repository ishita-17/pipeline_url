#!/usr/bin/python3

from __future__ import absolute_import
from pipeline_url.celeryapp import app

import json
import pymongo
import requests

#from celery.schedules import crontab

@app.task
def url_access(url):
    r = requests.get(url)
    
    d = json.loads(r.text)  #Converting string to dictionary

    items = d["result"]["items"]  #Getting dictionary of all items

    client = pymongo.MongoClient()

    mydb = client["mydatabase"]

    mycol = mydb["urls"]

    for item in items:
        mycol.insert_one(item)  #Inserting each item in collection
        
    print("Successfully added to database.")
    
# add "url_access" task to the beat schedule
'''
app.conf.beat_schedule = {
    "url-task": {
        "task": "task.url_access",
        "schedule": crontab(minute = "*/5")
    }
}


To start program:
Run on one terminal window: celery -A task beat --loglevel=info
Run on another terminal window: celery -A task worker --loglevel=info

'''