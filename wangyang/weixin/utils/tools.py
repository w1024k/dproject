# coding=utf-8

from django.core.cache import cache
import wechatpy
from weixin import settings
from common import settings as common_settings
from common.models import DailyCount
from common.utils import get_redis
from datetime import datetime, timedelta


class WeixinClient(wechatpy.WeChatClient):
    def __init__(self, appid, secret, access_token=None, session=None):
        super(WeixinClient, self).__init__(appid, secret, access_token, session)

    @staticmethod
    def instance():
        if not hasattr(WeixinClient, '_instance'):
            appid = settings.APPID
            secret = settings.APPSECRET
            access_token = WeixinClient(appid, secret).get_access_token()
            setattr(WeixinClient, '_instance', WeixinClient(appid, secret, access_token=access_token))
        return getattr(WeixinClient, '_instance')

    def get_access_token(self):
        access_token = cache.get(settings.ACCESS_TOKE_CACHE_KEY)
        if not access_token:
            access_token_data = self.fetch_access_token()
            access_token = access_token_data['access_token']
            timeout = access_token_data['expires_in'] - 100
            cache.set(settings.ACCESS_TOKE_CACHE_KEY, access_token, timeout=timeout)
        return access_token


class EventHandler(object):
    def __init__(self, event_key):
        self.key = event_key

    def get_event_handler(self):
        event_func_mapping = {
            settings.EventEnum.DAILY_VISIT_COUNT: self.daily_count
        }
        handle_func = event_func_mapping[self.key]
        return handle_func()

    def daily_count(self):
        yesterday = datetime.today().date() + timedelta(-1)
        yesterday_count = DailyCount.objects.only('count').get(date=yesterday,
                                                               event=common_settings.CountEventEnum.URL_VISIT).count
        return yesterday_count
