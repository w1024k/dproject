# coding=utf-8
import os
import json
from django.shortcuts import render
from django.http.response import HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings
from django.template.context_processors import request
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def download_list(request, template="cloud/file_list.html"):
    source = request.GET.get("source", "")
    if not source:
        dir_source = settings.DOWNLOAD_SOURCE_DIR
    else:
        dir_source = os.path.join(settings.DOWNLOAD_SOURCE_DIR, source)
    
    records = []
    dir_iter = os.walk(dir_source)
    _, dirs, files = dir_iter.next()
    for file_name in files:
        record = dict(
                name=file_name,
                link=os.path.join(settings.SOURCE_HOST, os.path.join(source, file_name)),
                property=0
            )
        
        records.append(record)
        
    for dir_name in dirs:
        record = dict(
                name=dir_name,
                link=reverse("cl_download_list") + '?source=' + os.path.join(source, dir_name),
                property=1
            )
        records.append(record)
    data = dict(records=records)
#     return HttpResponse(json.dumps(records), content_type='application/json')
    return render(request, template, context=data)


def upload_index(request, template="cloud/upload_index.html"):
    return render(request, template)


@csrf_exempt
def upload_part_file(request, template="cloud/upload_index.html"):
    task_id = request.POST.get("task_id")
    chunk = request.POST.get("chunk", 0)
    filename = "%s%s" % (task_id, chunk)
    upload_file = request.FILES.get("file")
    store_dir = os.path.join(settings.TMP_DIR, filename)
    with open(store_dir, 'wb') as f:
        for c in upload_file.chunks():
            f.write(c)
    return render(request, template)

    
@csrf_exempt
def upload_merge_file(request, template="cloud/upload_index.html"):
    target_filename = request.GET.get("filename")
    task_id = request.GET.get("filename")
    chunk = 0
    store_dir = os.path.join(settings.DOWNLOAD_SOURCE_DIR, target_filename)
    with open(store_dir, 'wb') as target_file:
        while True:
            try:
                filename = "%s%s" % (task_id, chunk)
                source_file = open(os.path.join(settings.TMP_DIR, filename))
                target_file.write(source_file.read())
                source_file.close()
            except IOError, e:
                break
            
            chunk += 1
            os.remove(filename)
    return render(request, template)
