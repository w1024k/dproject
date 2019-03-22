#!/usr/bin/env python
# coding: utf-8

import copy
import json

from django.http import HttpResponse

from weixin import settings
from weixin.utils import weixin_sign


def get_sign(request):
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    url = request.POST.get('url')
    rsp_data['data'] = weixin_sign.sign_detail_dict(url)
    return HttpResponse(json.dumps(rsp_data), content_type='application/json')
