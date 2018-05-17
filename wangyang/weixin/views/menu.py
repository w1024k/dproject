# coding: utf-8
from weixin.utils import tools
from weixin import settings
import copy
from django.http import HttpResponse
import ujson as json


def create_menu(reuqest):
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    client = tools.WeixinClient.instance()
    menu_data = ''
    rsp = client.menu.create(menu_data)
    print rsp
    return HttpResponse(json.dumps(rsp_data), content_type='application/json')
