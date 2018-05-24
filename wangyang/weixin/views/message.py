# coding=utf-8
from django.http import HttpResponse
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from weixin import settings, tasks
import wechatpy
from common.tools import auto_answer
from common.models import OpenUser
from common import settings as common_setting
from weixin.utils import tools


def notify(request):
    if request.method == 'GET':
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
        try:
            check_signature(settings.TOKEN, signature, timestamp, nonce)
        except InvalidSignatureException:
            return HttpResponse('')
        return HttpResponse(echostr)
    else:
        receive_msg = wechatpy.parse_message(request.body)
        # 收到文本,自动回复
        if isinstance(receive_msg, wechatpy.messages.TextMessage):
            content = auto_answer.answer_robot(receive_msg.content)
            reply = wechatpy.replies.TextReply(content=content, message=receive_msg)
            return HttpResponse(reply.render())
        # 关注事件
        elif isinstance(receive_msg, wechatpy.events.SubscribeEvent):
            receive_msg.msgtype = 'text'
            reply = wechatpy.replies.TextReply(content=settings.ANSWER_MSG_LIST['SUBSCRIBE'], message=receive_msg)
            tasks.create_weixin_user.delay(receive_msg.source)
            return HttpResponse(reply.render())
        # 取消关注
        elif isinstance(receive_msg, wechatpy.events.UnsubscribeEvent):
            OpenUser.objects.filter(supplier=common_setting.SupplierEnum.WECHAT, openid=receive_msg.source).update(
                state=common_setting.StateEnum.DELETED)
            return HttpResponse('')

        # 扫描带参数二维码(已关注,未关注,未关注微信会提示关注) 可用于扫码登录
        elif isinstance(receive_msg, (wechatpy.events.ScanEvent, wechatpy.events.SubscribeScanEvent)):
            return HttpResponse('')

        elif isinstance(receive_msg, (wechatpy.events.LocationEvent, wechatpy.events.LocationSelectEvent)):
            print receive_msg
            receive_msg.msgtype = 'text'
            reply = wechatpy.replies.TextReply(content=u'位置上报成功', message=receive_msg)
            return HttpResponse(reply.render())

        elif isinstance(receive_msg, wechatpy.events.ClickEvent):

            event_handler = tools.EventHandler(receive_msg.key)
            visit_count = event_handler.get_event_handler()

            receive_msg.msgtype = 'text'
            reply = wechatpy.replies.TextReply(content=settings.ANSWER_MSG_LIST['SUBSCRIBE'] % str(visit_count),
                                               message=receive_msg)

            return HttpResponse(reply.render())

        else:
            receive_msg.msgtype = 'text'
            reply = wechatpy.replies.TextReply(content=settings.ANSWER_MSG_LIST['PARSE_FAIL'], message=receive_msg)
            return HttpResponse(reply.render())
