# coding=utf-8

from django.core.cache import cache
import wechatpy
from weixin import settings


class WeixinClient(wechatpy.WeChatClient):
    def __init__(self, appid, secret, access_token=None, session=None):
        super(WeixinClient, self).__init__(appid, secret, access_token, session)

    @staticmethod
    def instance():
        if not hasattr(WeixinClient, '_instance'):
            appid = settings.APPID
            secret = settings.APPSECRET
            print appid, 111
            print secret, 222
            access_token = WeixinClient(appid, secret).get_access_token()
            setattr(WeixinClient, '_instance',
                    WeixinClient(appid, secret, access_token=access_token))
        return getattr(WeixinClient, '_instance')

    def get_access_token(self):
        access_token = cache.get(settings.ACCESS_TOKE_CACHE_KEY)
        if not access_token:
            access_token_data = self.fetch_access_token()
            access_token = access_token_data['access_token']
            timeout = access_token_data['expires_in'] - 100
            cache.set(settings.ACCESS_TOKE_CACHE_KEY, access_token, timeout=timeout)
        return access_token
