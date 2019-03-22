# coding=utf-8

from settings_common import *

REDIS_HOST = "redis"
MYSQL_HOST = "mysql"
AL_HOST = "172.16.255.43"

# STATIC_URL = 'http://static.w1024k.top/static/'
# 使用https 免费版只支持一个域名

STATIC_HOST = "http://static.w1024k.top/"
STATIC_URL = '/static/'
PROJECT_VERSION = '001v01'
# 搜集目录
STATIC_ROOT = '/media/www/static/'

# app目录 额外的静态文件
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# 微信公众号配置
TOKEN = 'wangyang'
APPID = 'wx2d7d831e6aceea11'
APPSECRET = '44d7ab4231ab6709e306938f97e505a6'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')

# cloud
TMP_DIR = '/media/www/tmp/'
DOWNLOAD_SOURCE_DIR = '/media/www/source/'
SOURCE_HOST = '/source/'


BROKER_URL = 'redis://:redis@%s:6379/0' % REDIS_HOST
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_IGNORE_RESULT = True

CACHES["default"]["LOCATION"] = "%s:6379:1" % REDIS_HOST
DATABASES["default"]["HOST"] = MYSQL_HOST
