from django.shortcuts import render
from django.http import HttpResponse
import itchat
import os
import threading
from wechat import settings as wechat_setting


def login(request):
    login_thread = threading.Thread(target=itchat.auto_login,
                                    kwargs=(dict(hotReload=True,
                                                 picDir=wechat_setting.PIC_DIR)))
    while os.path.exists(wechat_setting.PIC_DIR):
        pic = open(wechat_setting.PIC_DIR, 'rb')
        response = HttpResponse(pic, content_type='image/jpeg')
        return response
