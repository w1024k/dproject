# coding=utf-8
from django.db import models
from abstract import *
from common import settings


# Create your models here.
class UrlVisitCount(TimeModel):
    client_ip = models.GenericIPAddressField(default=settings.DEFAULT_IP, verbose_name=u'客户端IP')
    url = models.CharField(default=settings.DEFAULT_URL, max_length=128, verbose_name=u'链接地址')

    class Meta:
        verbose_name = u'链接访问数据统计'
        verbose_name_plural = u'链接访问数据统计'

    def __unicode__(self):
        return self.client_ip


class DailyCount(models.Model):
    date = models.DateField(db_index=True, verbose_name=u'日期')
    count = models.IntegerField(default=0, verbose_name=u'总数')
    event = models.PositiveSmallIntegerField(choices=settings.COUNT_EVENT_CHOICES, db_index=True,
                                             verbose_name=u'统计事件类型')

    class Meta:
        verbose_name = u'每日数据统计'
        verbose_name_plural = u'每日数据统计'

    def __unicode__(self):
        return '%s-%s' % (self.date, self.event)
