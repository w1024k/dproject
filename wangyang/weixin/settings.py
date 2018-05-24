# coding=utf-8
from django.conf import settings

TOKEN = 'wangyang'

APPID = 'wx998081831c4cc310'
APPSECRET = 'f022d5490574a310cdd57a311670b0e1'

# if hasattr(settings, "TOKEN"):
#     TOKEN = settings.TOKEN
#
# if hasattr(settings, "APPID"):
#     APPID = settings.APPID
#
# if hasattr(settings, "APPSECRET"):
#     APPSECRET = settings.APPSECRET

ERROR = {}

ERROR.update(settings.ERROR)

# MSG_TYPE = (
#     'image',
#     'voice',
#     'video',
#     'shortvideo',
#     'location',
#     'link',
# )

ANSWER_MSG_LIST = {
    'PARSE_FAIL': '我现在只方便看文字',
    'SUBSCRIBE': '感谢你的关注',
    'VISIT_COUNT': '昨日访问量为%s次'
}

ACCESS_TOKE_CACHE_KEY = 'weixin.access.token.key'


class EventEnum:
    DAILY_VISIT_COUNT = 'HELLO_ALWAYS_YESTERDAY_VISIT'
    LOCATION_WEATHER = 'HELLO_ALWAYS_WEATHER'
    SUBMIT_LOCATION = ''
