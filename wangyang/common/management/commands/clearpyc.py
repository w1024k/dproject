# coding=utf-8

import os

from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
    help = '用户删除项目目录下的pyc文件'
    requires_model_validation = False

    def handle_noargs(self, **options):
        from django.conf import settings

        print "remove *.pyc file"
        for root, dirs, files in os.walk(settings.BASE_DIR):
            # if '__init__.py' not in files:
            #    continue
            for fname in files:
                if (os.path.splitext(fname)[1] == ".pyc") or (os.path.splitext(fname)[1] == ".pyo"):
                    del_file = os.path.join(root, fname)
                    print "Delete:", del_file
                    os.remove(del_file)
