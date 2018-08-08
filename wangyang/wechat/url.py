# coding=utf-8


from django.conf.urls import url
from views import chat

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^itchat/login/$', chat.login, name=""),
]
