# coding=utf-8

from django.conf.urls import url
from cloud import views as cl

urlpatterns = [
    url(r'^download/list/$', cl.download_list, name="cl_download_list"),
    url(r'^upload/index/$', cl.upload_index, name="cl_upload_index"),
    url(r"^upload/part/file/$", cl.upload_part_file, name="cl_upload_part_file"),
    url(r"^upload/merge/$", cl.upload_merge_file, name="cl_upload_merge")
]
