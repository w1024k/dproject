# coding=utf-8
from celery import task
from common.models import OpenUser, Profile
from common import settings
from common.tools.common_tool import create_random_string
from weixin import settings as weixin_setting
from django.contrib.auth.models import User
from weixin.utils import tools
import logging
import wechatpy
from django.db import transaction

django_log = logging.error('django')


@task
def create_weixin_user(uid):
    client = tools.WeixinClient.instance()
    weixin_user = wechatpy.client.api.WeChatUser(client)
    try:
        open_user = OpenUser.objects.get(supplier=settings.SupplierEnum.WECHAT, uid=uid)
    except OpenUser.DoesNotExist:
        username = 'weixin_%s' % create_random_string(digits=10)
        with transaction.atomic():
            user = User.objects.create(first_name=weixin_user['nickname'], username=username)
            OpenUser.objects.create(
                supplier=settings.SupplierEnum.WECHAT,
                nickname=weixin_user['nickname'],
                user=user,
                uid=uid,
            )
            Profile.objects.create(user=user,
                                   avatar_path=weixin_user['headimgurl'],
                                   address='-'.join([weixin_user['country'], weixin_user['province'], weixin_user['city']]),
                                   sex=weixin_user['sex'] if weixin_user['sex'] in [settings.SexEnum.WOMAN,
                                                                                    settings.SexEnum.MAN] else settings.SexEnum.OTHER, )
    else:
        open_user.state = settings.StateEnum.VALID
        open_user.save()
