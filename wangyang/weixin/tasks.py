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
def create_weixin_user(openid):
    client = tools.WeixinClient.instance()
    weixin_user = wechatpy.client.api.WeChatUser(client).get(openid)
    try:
        open_user = OpenUser.objects.get(supplier=settings.SupplierEnum.WECHAT, openid=openid)
    except OpenUser.DoesNotExist:
        username = 'weixin_%s' % create_random_string(digits=10)
        with transaction.atomic():
            user = User.objects.create(first_name=weixin_user['nickname'], username=username)
            OpenUser.objects.create(
                supplier=settings.SupplierEnum.WECHAT,
                nickname=weixin_user['nickname'],
                user=user,
                openid=openid,
            )
            if int(weixin_user['sex']) in [settings.SexEnum.WOMAN, settings.SexEnum.MAN]:
                sex = int(weixin_user['sex'])
            else:
                sex = settings.SexEnum.OTHER

            Profile.objects.create(user=user,
                                   avatar_path=weixin_user['headimgurl'],
                                   address='-'.join(
                                       [weixin_user['country'], weixin_user['province'], weixin_user['city']]),
                                   sex=sex)
    else:
        open_user.state = settings.StateEnum.VALID
        open_user.save()
