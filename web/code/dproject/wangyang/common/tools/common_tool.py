# coding=utf-8
import os
import re
import random


def create_random_string(digits=10):
    chars = random.sample(
        ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e',
         'd', 'c', 'b', 'a', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], digits)
    return ''.join(chars)


def kill_process(port):
    process_detail_list = os.popen('lsof -i:%s' % port).readlines()
    regex = re.compile('\s+')
    process_id_list = []
    if len(process_detail_list) > 1:
        for process_detail in process_detail_list:
            process = regex.split(process_detail)
            process_id = process[1]
            if process_id.isdigit():
                process_id_list.append(process_id)

    for pid in set(process_id_list):
        try:
            print pid
            os.system('kill -9 %s' % pid)
        except Exception as e:
            print e
