# coding=utf-8

from django.core.management.base import NoArgsCommand
from common.utils import get_redis
from common.models import DailyCount
from common import settings
from datetime import datetime, timedelta


class Command(NoArgsCommand):
    help = '更新每日每日站点访问数统计'

    def handle_noargs(self, **options):
        r = get_redis()
        count = int(r.get(settings.URL_VISIT_DAILY_COUNT_KEY))
        yesterday = datetime.today().date() + timedelta(-1)
        try:
            DailyCount.objects.create(date=yesterday, count=count, event=settings.CountEventEnum.URL_VISIT)
        except Exception as e:
            print e
        else:
            r.set(settings.URL_VISIT_DAILY_COUNT_KEY, 0)
