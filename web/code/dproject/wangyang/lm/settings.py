# coding=utf-8
from django.conf import settings

LM_HOST = 'http://120.27.18.252:5678'

LOGIN_URL = "/rest/user/login/"

CANDIDATE_URL = '/rest/candidate/list/'

JOBORDER_URL = '/rest/joborder/list/'

HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}

ADMIN_EMAIL = "amanda"
ADMIN_PASSWORD = "888888"

ERROR = {
    'API_ERROR': {'code': '20001', 'msg': u'调用接口失败'},
}

ERROR.update(settings.ERROR)
