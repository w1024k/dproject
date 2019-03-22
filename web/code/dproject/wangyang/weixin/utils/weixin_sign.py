#!/usr/bin/env python
# coding: utf-8

import hashlib
import logging
import random
import requests
import string
import time

from django.core.cache import cache

from weixin import settings


django_log = logging.getLogger('django')


def make_jsapi_ticket():
    jsapi_ticket = cache.get('panorma_weixin_jsapi_ticket')
    if not jsapi_ticket:
        access_toke = cache.get('panorama_weixin_acess_toke')
        if not access_toke:
            access_params = {
                "grant_type": "client_credential",
                "appid": settings.APPID,
                "secret": settings.APPSECRET,
            }
            try:
                r = requests.get(settings.ACCESS_TOKE_URL, params=access_params)
                access_toke = r.json()['access_token']
            except Exception as e:
                django_log.error('调用微信接口,获取access_token失败:', e)
                return None
            cache.set('panorama_weixin_acess_toke', access_toke, settings.weixin_sign_timeout)
            
        try:
            jsapi_params = {
                "access_token": access_toke,
                "type": "jsapi"
            }
            r = requests.get(settings.JSAPI_TICKET_URL, params=jsapi_params)
            jsapi_ticket = r.json()['ticket']
        except Exception as e:
            django_log.error('调用微信接口,获取jsapi_ticket失败:', e)
            return None
        cache.set('panorma_weixin_jsapi_ticket', jsapi_ticket, settings.weixin_sign_timeout)

    return jsapi_ticket


class Sign:
    def __init__(self, jsapi_ticket, url):
        self.ret = {
            'nonceStr': self.__create_nonce_str(),
            'jsapi_ticket': jsapi_ticket,
            'timestamp': self.__create_timestamp(),
            'url': url
        }

    def __create_nonce_str(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

    def __create_timestamp(self):
        return int(time.time())

    def sign(self):
        string = '&'.join(['%s=%s' % (key.lower(), self.ret[key]) for key in sorted(self.ret)])
        self.ret['signature'] = hashlib.sha1(string).hexdigest()
        return self.ret


def sign_detail_dict(url):
    sign_params = {}
    jsapi_ticket = make_jsapi_ticket()
    if jsapi_ticket:
        sign = Sign(jsapi_ticket, url)
        sign = sign.sign()
        sign_params.update({'appId':settings.APPID})
        sign_params.update(sign)

    return sign_params
