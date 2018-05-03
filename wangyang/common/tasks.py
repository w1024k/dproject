# coding: utf-8

import time
from celery import task
from common.models import DailyCount
import datetime


# @task
# def daily_increase(event):
#     today = datetime.datetime.now().date()
#     if not DailyCount.objects.filter(event=event,date=today).update(count=)

