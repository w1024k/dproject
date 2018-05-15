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

django_log = logging.error('django')


@task
def create_weixin_user(uid):
    client = wechatpy.WeChatClient(appid=weixin_setting.APPID, secret=weixin_setting.APPSECRET,
                                   access_token=tools.get_access_token())
    weixin_user = wechatpy.client.api.WeChatUser(client)
    try:
        open_user = OpenUser.objects.get(supplier=settings.SupplierEnum.WECHAT, uid=uid)
    except OpenUser.DoesNotExist:
        username = 'weixin_%s' % create_random_string(digits=10)
        user = User.objects.create(first_name=weixin_user['nickname'], username=username)
        OpenUser.objects.create(
            supplier=settings.SupplierEnum.WECHAT,
            nickname=weixin_user['nickname'],
            user=user,
            uid=uid,
        )
        Profile.objects.create(user=user)
    else:
        open_user.state = settings.StateEnum.VALID
