# -*- coding: utf-8 -*-
import os.path
import sys
import redis
if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import hashlib
import mongoengine
import settings


def connect_db():
    mongoengine.connect(settings.DB_NAME, host=settings.DB_ADDRESS, port=settings.DB_PORT)


def md5(astring):
    return hashlib.md5(astring).hexdigest()


def connect_redis():
    pool = redis.ConnectionPool(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)
    r = redis.Redis(connection_pool=pool)
    return r

if __name__ == "__main__":
    connect_redis()
