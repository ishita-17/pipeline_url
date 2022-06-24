from __future__ import absolute_import
from celery import Celery

app = Celery('pipeline', 
             broker='pyamqp://guest@localhost//',
             include=["pipeline.tasks.py"])  