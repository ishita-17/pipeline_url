#!/usr/bin/python3

from __future__ import absolute_import
from celery import Celery

app = Celery('pipeline_url', 
             broker='pyamqp://guest@localhost//',
             include=["pipeline_url.tasks"])  