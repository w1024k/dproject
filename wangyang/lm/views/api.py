# coding=utf-8

import copy
import ujson as json
from django.http import HttpResponse
from django.conf import settings


def upload_image(request):
    f1 = request.FILES['pic']
    name = '%s/%s' % (settings.MEDIA_ROOT, f1.name)
    with open(name, 'w') as pic:
        for c in f1.chunks():
            pic.write(c)
    return HttpResponse("ok")
