# coding=utf-8

from django.core.management.base import NoArgsCommand
from common.models import UrlVisitCount
from datetime import datetime, timedelta


# 0 0 1 * * su wang;/home/wang/.pyenv/versions/web/bin/python /home/wang/repositories/dproject/wangyang/manage.py clear_visit_count;exit

class Command(NoArgsCommand):
    help = '删除一个月前的访问记录'

    def handle_noargs(self, **options):
        clear_date = datetime.today().date() + timedelta(-30)
        UrlVisitCount.objects.filter(create_time__lt=clear_date).delete()
