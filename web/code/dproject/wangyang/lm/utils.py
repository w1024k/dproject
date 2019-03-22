# coding=utf-8
import requests, os
import ujson as json
from lm import settings


def raw_url(url):
    return settings.LM_HOST + url


class Session(object):
    @staticmethod
    def get_session():
        if not hasattr(Session, "_session"):
            session = requests.session()
            data = {"data": json.dumps(
                {"email": settings.ADMIN_EMAIL, "password": settings.ADMIN_PASSWORD, "remember": False})}
            session.post(raw_url(settings.LOGIN_URL), data=data, headers=settings.HEADER)
            Session._session = session
        return Session._session


def get_session():
    return Session.get_session()
