# coding=utf-8

from django.core.cache import cache
import wechatpy
from weixin import settings


def get_access_token():
    access_token = cache.get(settings.ACCESS_TOKE_CACHE_KEY)

    if not access_token:
        client = wechatpy.WeChatClient(appid=settings.APPID, secret=settings.APPSECRET)
        access_token_data = client.fetch_access_token()
        access_token = access_token_data['access_token']
        timeout = access_token_data['expires_in'] - 100
        cache.set(settings.ACCESS_TOKE_CACHE_KEY, access_token, timeout=timeout)
    return access_token
