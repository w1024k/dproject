# coding=utf-8
from django.conf import settings

TOKEN = 'wangyang'

APPID = 'wx998081831c4cc310'
APPSECRET = 'wx998081831c4cc310'

if hasattr(settings, TOKEN):
    TOKEN = settings.TOKEN

if hasattr(settings, APPID):
    APPID = settings.APPID

if hasattr(settings, APPSECRET):
    APPSECRET = settings.APPSECRET

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
    'PARSE_FAIL': u'我现在只方便看文字',
    'SUBSCRIBE': u'感谢你的关注',
}

ACCESS_TOKE_CACHE_KEY = 'weixin.access.token.key'