# coding=utf-8

from django.core.management.base import NoArgsCommand
from common.utils import get_redis
from common.models import DailyCount
from common import settings
from datetime import datetime, timedelta


# 0 0 * * * su wang;/home/wang/.pyenv/versions/web/bin/python /home/wang/repositories/dproject/wangyang/manage.py update_visit_count;exit

class Command(NoArgsCommand):
    help = '更新每日每日站点访问数统计'

    def handle_noargs(self, **options):
        r = get_redis()
        count = int(r.get(settings.URL_VISIT_DAILY_COUNT_KEY))
        yesterday = datetime.today().date() + timedelta(-1)
        try:
            DailyCount.objects.create(date=yesterday, count=count, event=settings.CountEventEnum.URL_VISIT)
        except Exception as e:
            # TODO 之后加一个发送到微信的功能
            print e
        else:
            r.set(settings.URL_VISIT_DAILY_COUNT_KEY, 0)
