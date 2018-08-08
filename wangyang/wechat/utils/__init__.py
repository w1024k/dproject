# coding=utf-8
from wechat import settings
import os


def clean_login_record():
    if os.path.exists(settings.PIC_DIR):
        os.remove(settings.PIC_DIR)
    if os.path.exists(settings.PKL):
        os.remove(settings.PKL)
