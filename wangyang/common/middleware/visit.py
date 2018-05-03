# coding: utf-8


from django.conf import settings
from common.models import UrlVisitCount


class VisitCount(object):
    def process_request(self, request):
        path = request.META['PATH_INFO']
        if not path.startswith('/wangyang/admin/'):

            # 被nginx代理时取真实IP
            if request.META.has_key('HTTP_X_FORWARDED_FOR'):
                forwarded_for_ips = request.META['HTTP_X_FORWARDED_FOR'].split(',')
                if len(forwarded_for_ips) >= 2:
                    real_ip = forwarded_for_ips[0].strip()
                    if real_ip:
                        request.META['REMOTE_ADDR'] = real_ip

            ip = request.META['REMOTE_ADDR']
        print 111
        print request.META['REMOTE_ADDR']
