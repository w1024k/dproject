# coding: utf-8
import uuid
import redis
from common import settings


def create_uuid():
    return str(uuid.uuid1()).replace('-', '')


class RedisClient(object):
    @staticmethod
    def get_client():
        if not hasattr(RedisClient, "_redisClient"):
            redisClient = redis.Redis(host='localhost', port=6379, db=3, password='redis')
            # if not redisClient.get(settings.URL_VISIT_DAILY_COUNT_KEY):
            #     redisClient.set(settings.URL_VISIT_DAILY_COUNT_KEY, 0)
            RedisClient._redisClient = redisClient

        return RedisClient._redisClient


def get_redis():
    return RedisClient.get_client()
