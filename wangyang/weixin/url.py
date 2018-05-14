# coding=utf-8


from django.conf.urls import url
from views import message

from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    url(r'^message/notify/', csrf_exempt(message.notify), name="weixin_notify"),
]
