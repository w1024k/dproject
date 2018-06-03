# coding=utf-8

from .settings_base import *

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {  # 日志格式
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
    },
    'filters': {  # 过滤器
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {  # 处理器
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'mail_admins': {  # 发送邮件通知管理员
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],  # 仅当 DEBUG = False 时才发送邮件
            'include_html': True,
        },
        'info_handler': {  # 记录到文件
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'info.log'),
            'filters': ['require_debug_false'],
            'formatter': 'standard',
        },
        # 'console': {  # 输出到控制台
        #     'level': 'ERROR',  # 设为debug时,一些数据的查询信息之类的信息都会被打印
        #     'class': 'logging.StreamHandler',
        #     'formatter': 'standard',
        # },
    },
    'loggers': {  # logging管理器
        'django': {
            'handlers': ['info_handler'],
            'level': 'ERROR',
            # 'propagate': False
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # 对于不在 ALLOWED_HOSTS 中的请求不发送报错邮件
        'django.security.DisallowedHost': {
            'handlers': ['null'],
            'propagate': False,
        },
    }
}

# 管理员邮箱
ADMINS = (
    ('wangyang', 'w1024k@163.com'),
)

# 非空链接，却发生404错误，发送通知MANAGERS
SEND_BROKEN_LINK_EMAILS = True
MANAGERS = ADMINS

# Email设置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 465  # SMTP服务端口
EMAIL_HOST_USER = 'wangyangpublic@163.com'  # 我的邮箱帐号
EMAIL_HOST_PASSWORD = 'wangyang001'  # 授权码
EMAIL_USE_TLS = True  # 开启安全链接
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # 设置发件人

STATIC_URL = 'http://static.wangyang.com/static/'
# 搜集目录
STATIC_ROOT = '/www/media/wang/static/'

# app目录 额外的静态文件
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# 微信公众号配置
TOKEN = 'wangyang'
APPID = 'wx2d7d831e6aceea11'
APPSECRET = '44d7ab4231ab6709e306938f97e505a6'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
