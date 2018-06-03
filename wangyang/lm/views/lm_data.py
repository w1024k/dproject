# coding=utf-8

from django.http import HttpResponse
import ujson as json
import copy
from lm import settings, utils as lm_utils


# Create your views here.

def jobs(request):
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    page = request.GET.get('page', 1)
    params = {
        'byfilter': '-8888',
        'ordering': '-lastUpdateDate',
        'paginate_by': 10,
        'page': page
    }
    session_request = lm_utils.get_session()
    try:
        jobs = session_request.get(url=lm_utils.raw_url(settings.JOBORDER_URL), params=params).json()
    except Exception as e:
        rsp_data = copy.copy(settings.ERROR['API_ERROR'])
        rsp_data['msg'] = e
        return HttpResponse(json.dumps(rsp_data), content_type='application/json')

    records = list()
    for record in jobs['list']:
        detail = {
            'job_name': record["jobTitle"],
            'company': record['client']['name'],
            'city': record['city'] and record['city']['name'],
            'waiter': [user["user"]["chineseName"] for user in record['users']],
            'worker_count': record['currentCount'],
            'lastupdate': record['lastUpdate'],
        }
        records.append(detail)
    rsp_data["data"] = {'records': records}
    return HttpResponse(json.dumps(rsp_data), content_type='application/json')


def candidate(request):
    rsp_data = copy.copy(settings.ERROR['SUCC'])
    page = request.GET.get('page', 1)
    params = {
        'byfilter': '-8888',
        'ordering': '-lastUpdateDate',
        'paginate_by': 10,
        'page': page
    }
    session_request = lm_utils.get_session()
    try:
        candidates = session_request.get(url=lm_utils.raw_url(settings.CANDIDATE_URL), params=params).json()
    except Exception as e:
        rsp_data = copy.copy(settings.ERROR['API_ERROR'])
        rsp_data['msg'] = e
        return HttpResponse(json.dumps(rsp_data), content_type='application/json')

    records = list()
    for record in candidates['list']:
        detail = {
            'name': record['chineseName'],
            'company': record['company']['name'],
            'job': record['current']['title'],
            'city': record['city'] and record['city']['name'],
            'salary': record['annualSalary'],
            'age': record['dateOfBirth'],
            'phone': record['mobile'],
            'last_contact': record['lastUpdate'],

            'gender': '男' if record['gender'] else '女',
            'school': record['school'],
            'email': record['email'],
            'education': record['education']['value'],
        }
        records.append(detail)
    rsp_data["data"] = {'records': records}
    return HttpResponse(json.dumps(rsp_data), content_type='application/json')
