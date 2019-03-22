# coding=utf-8

import requests
from common import settings
import logging
import re

django_log = logging.getLogger('django')


def answer_robot(keyword):
    try:
        url = settings.ROBOT_API + keyword
        rsp = requests.get(url=url).json()
        content = rsp['content']
        content = re.sub('{br}', '\n', content)
    except Exception as e:
        django_log.error(e)
        content = settings.ROBOT_API_ERROR
    return content
