# coding=utf-8


from django.conf.urls import url
from views import message, share

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^message/notify/$', csrf_exempt(message.notify), name="weixin_notify"),
    url(r'^get/sign/$', csrf_exempt(share.get_sign), name="weixin_get_sign"),
]
