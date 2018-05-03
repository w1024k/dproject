# coding: utf-8

class StateEnum:
    VALID = 0
    TEMPORARY = 1
    DELETED = 9


STATE_CHOICES = (
    (StateEnum.VALID, u'有效'),
    (StateEnum.TEMPORARY, u'临时记录'),
    (StateEnum.DELETED, u'删除'),
)

DEFAULT_IP = '0.0.0.0'
DEFAULT_URL = '/wangyang/'


class CountEventEnum:
    URL_VISIT = 1


COUNT_EVENT_CHOICES = (
    (CountEventEnum.URL_VISIT, u'链接访问数')
)
