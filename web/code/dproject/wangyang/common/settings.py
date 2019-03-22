# coding: utf-8
import redis
from django.conf import settings


class RedisClient(object):
    @staticmethod
    def get_client():
        if not hasattr(RedisClient, "_redisClient"):
            redis_client = redis.Redis(host=settings.REDIS_HOST, port=6379, db=3, password='redis')
            RedisClient._redisClient = redis_client

        return RedisClient._redisClient


REDIS_CLI = RedisClient.get_client()


class StateEnum:
    VALID = 0
    TEMPORARY = 1
    DELETED = 9


STATE_CHOICES = (
    (StateEnum.VALID, u'有效'),
    (StateEnum.TEMPORARY, u'临时记录'),
    (StateEnum.DELETED, u'删除'),
)


class SupplierEnum:
    WECHAT = 1
    ALIPAY = 2
    SINA = 3
    OTHER = 4


SUPPLIER_CHOICES = (
    (SupplierEnum.WECHAT, u'微信'),
    (SupplierEnum.ALIPAY, u'支付宝'),
    (SupplierEnum.SINA, u'新浪'),
    (SupplierEnum.OTHER, u'其他'),
)


class SexEnum:
    MAN = 1
    WOMAN = 2
    OTHER = 0


SEX_CHOICES = (
    (SexEnum.MAN, '男'),
    (SexEnum.WOMAN, '女'),
    (SexEnum.OTHER, '其他'),
)

DEFAULT_IP = '0.0.0.0'
DEFAULT_URL = '/wangyang/'


class CountEventEnum:
    URL_VISIT = 1


COUNT_EVENT_CHOICES = (
    (CountEventEnum.URL_VISIT, u'网站总访问数'),
)

URL_VISIT_DAILY_COUNT_KEY = "url.visit.daily.count"

ROBOT_API = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg='
ROBOT_API_ERROR = u'机器人客服打盹了'

DEFAULT_AVATAR_PATH = '/static/images/avatar.jpg'

QINIU_ACCESSKEY = 'JkmVZKPlN7lHIq2s15UXe4ocRSPX0IgKyIBbPw_8'
QINIU_SECRETKEY = 'BQL-mTutx_woOqAPoea4UmH5CTIx9P6Ls-RmpsC8'
BUCKET_NAME = 'wangyang'
