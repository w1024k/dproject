# coding=utf-8

from django.conf.urls import url
from . import views as lm

urlpatterns = [
    url(r'^jobs/', lm.jobs, name="lm_jobs"),
    url(r'^candidate/', lm.candidate, name="lm_candidate"),
]
