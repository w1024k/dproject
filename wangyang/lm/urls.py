# coding=utf-8

from django.conf.urls import url
from lm.views import lm_data as lm, api

urlpatterns = [
    url(r'^jobs/', lm.jobs, name="lm_jobs"),
    url(r'^candidate/', lm.candidate, name="lm_candidate"),
]

urlpatterns += [
    url(r'api/upload/', api.upload_image, name="api_upload_image")
]
