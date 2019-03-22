# coding=utf-8

'''
Created on 2019年1月16日

@author: Administrator
'''
import os
from django.conf import settings
from django_jinja import library


@library.global_function
def static(path, version='auto', static_url=None):
    static_url = static_url or settings.STATIC_URL
    
    if version == 'auto':
        url = '%s?v=%s' % (os.path.join(static_url, path), settings.PROJECT_VERSION)
    elif version == 'ignore':
        url = os.path.join(static_url, path)
    else:
        url = '%s%s?v=%s' % (static_url, path, version)
        
    return os.path.join(settings.STATIC_HOST, url)
