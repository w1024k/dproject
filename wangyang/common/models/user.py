# coding=utf-8
from django.db import models
from .abstract import TimeModel, StateModel
from common import settings
from django.contrib.auth.models import User


# Create your models here.

class OpenUser(TimeModel, StateModel):
    supplier = models.IntegerField(default=settings.SupplierEnum.WECHAT, choices=settings.SUPPLIER_CHOICES,
                                   verbose_name=u'账号来源')
    openid = models.CharField(max_length=128, verbose_name=u'第三方用户ID')
    ticket = models.CharField(default=u'', max_length=128, verbose_name=u'用户凭据')
    user = models.ForeignKey(User, verbose_name=u'关联的User')
    nickname = models.CharField(default=u'', max_length=32, verbose_name='昵称')

    class Meta:
        index_together = [('supplier', 'openid'), ]
        app_label = 'common'
        verbose_name = u'第三方账号'
        verbose_name_plural = u'第三方账号'

    def __unicode__(self):
        return u'%s,%s' % (self.supplier, self.openid)


class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name=u'关联User')
    sex = models.PositiveSmallIntegerField(default=settings.SexEnum.MAN, choices=settings.SEX_CHOICES,
                                           verbose_name=u'性别')
    mobile = models.CharField(default=u'', max_length=11, db_index=True, verbose_name=u'电话号码')
    wechat = models.CharField(default=u'', max_length=32, blank=True, verbose_name=u'微信')

    address = models.CharField(default=u'', max_length=64, blank=True, verbose_name=u'地址')
    avatar_path = models.CharField(default=settings.DEFAULT_AVATAR_PATH, max_length=256, verbose_name=u'头像文件')
    intro = models.TextField(default=u'', blank=True, verbose_name=u'个人简介')

    class Meta:
        app_label = "common"
        verbose_name = u'用户扩展表'
        verbose_name_plural = u'用户扩展表'

    def __unicode__(self):
        return u'%s(扩展)' % self.user.email
