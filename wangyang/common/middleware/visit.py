# coding: utf-8


from common import settings
from common.models import UrlVisitCount, DailyCount
from common.tasks import daily_visit_increase


class VisitCount(object):
    def process_request(self, request):
        path = request.META['PATH_INFO']
        print path.startswith('/wangyang/admin/')

        # 被nginx代理时取真实IP
        if request.META.has_key('HTTP_X_FORWARDED_FOR'):

            forwarded_for_ips = request.META['HTTP_X_FORWARDED_FOR'].split(',')
            if len(forwarded_for_ips) >= 2:
                real_ip = forwarded_for_ips[0].strip()
                if real_ip:
                    request.META['REMOTE_ADDR'] = real_ip
            else:
                request.META['REMOTE_ADDR'] = request.META['HTTP_X_FORWARDED_FOR']

        ip = request.META['REMOTE_ADDR']
        daily_visit_increase.delay(ip=ip, path=path)
