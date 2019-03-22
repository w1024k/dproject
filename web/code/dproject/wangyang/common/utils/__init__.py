# coding: utf-8
import uuid
import redis
import os
import re
from common import settings


def create_uuid():
    return str(uuid.uuid1()).replace('-', '')


def kill_port(port):
    port_detail = os.popen('lsof -i:%s' % port).read()
    if port_detail:
        raw_port = re.search(r'/usr/bin/ \d+', port_detail)
        if raw_port:
            thread_id = raw_port.group().split(' ')[1]
            os.system('kill -9 %s' % thread_id)
            return True
    return False
