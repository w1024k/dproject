# coding: utf-8


import pprint


from django.core.management import BaseCommand
from weixin.utils import tools
import ujson as json

menu_data = {
    "button": [
        {
            "type": "location_select",
            "name": u"今日天气",
            "key": "HELLO_ALWAYS_WEATHER"
        },
        {
            "name": u"菜单",
            "sub_button": [
                {
                    "type": "view",
                    "name": u"搜索",
                    "url": "http://www.baidu.com/"
                },
                {
                    "type": "view",
                    "name": "NBA",
                    "url": "http://nba.sina.cn/?vt=4"
                },
                {
                    "type": "click",
                    "name": u"昨日访问",
                    "key": "HELLO_ALWAYS_YESTERDAY_VISIT"
                },
            ]
        }]
}


class Command(BaseCommand):
    u'''
    更新微信公众号菜单内容
    '''

    def handle(self, *args, **options):
        menu_data_json = json.dumps(menu_data)
        pprint.pprint(menu_data)

        client = tools.WeixinClient.instance()
        s = client.menu.create(menu_data_json)
        print s
