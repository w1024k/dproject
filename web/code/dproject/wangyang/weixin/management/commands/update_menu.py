# coding: utf-8


import pprint

from django.core.management import BaseCommand
from weixin.utils import tools
import ujson as json

menu_data = {
    "button": [
        {
            "name": "菜单",
            "sub_button": [
                {
                    "type": "location_select",
                    "name": "今日天气",
                    "key": "HELLO_ALWAYS_WEATHER"
                },
                {
                    "type": "click",
                    "name": "昨日访问",
                    "key": "HELLO_ALWAYS_YESTERDAY_VISIT"
                },
            ]
        },
        {
            "name": "工具",
            "sub_button": [
                {
                    "type": "view",
                    "name": "搜索",
                    "url": "http://www.baidu.com/"
                },
                {
                    "type": "view",
                    "name": "NBA",
                    "url": "http://nba.sina.cn/?vt=4"
                },
                {
                    "type": "view",
                    "name": "低调看",
                    "url": "http://m.didiaokan.com/m.html"
                },
            ]
        }]
}


class Command(BaseCommand):
    u'''
    更新微信公众号菜单内容
    '''

    def handle(self, *args, **options):
        menu_data_json = json.dumps(menu_data, ensure_ascii=False)
        pprint.pprint(menu_data)

        client = tools.WeixinClient.instance()
        s = client.menu.create(menu_data_json)
        print s
