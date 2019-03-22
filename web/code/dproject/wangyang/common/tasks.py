# coding: utf-8

from celery import task
from redis import WatchError
from common.models import UrlVisitCount
from common import settings
import logging


@task
def daily_visit_increase(path, ip):
    try:
        UrlVisitCount.objects.create(url=path, client_ip=ip)
    except Exception as e:
        django_log = logging.getLogger('django')
        django_log.error(e)
    else:
        # 先放在redis里,用定时任务在表里创建记录
        with settings.REDIS_CLI.pipeline() as pipe:
            while True:
                pipe.watch(settings.URL_VISIT_DAILY_COUNT_KEY)
                try:
                    pipe.multi()
                    pipe.incr(settings.URL_VISIT_DAILY_COUNT_KEY)
                    pipe.execute()
                    break
                except WatchError as e:
                    pipe.unwatch()
