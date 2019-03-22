# encoding: utf-8

'''
为了避免所有的url请求都经过message middleware，所以采用当前的middleware，进对admin view设置消息
'''

from django.conf import settings
from django.contrib.messages.storage import default_storage


class AdminOnlyMessageMiddleware(object):
    def process_request(self, request):

        # path_info中以admin开头，才执行
        if request.META['PATH_INFO'].startswith('/wangyang/admin/'):
            request._messages = default_storage(request)

    def process_response(self, request, response):

        if request.META['PATH_INFO'].startswith('/wangyang/admin/'):
            if hasattr(request, '_messages'):
                unstored_messages = request._messages.update(response)
                if unstored_messages and settings.DEBUG:
                    raise ValueError('Not all temporary messages could be stored.')
        return response
