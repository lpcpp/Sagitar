# -*- coding: utf-8 -*-
import os.path
import sys
if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import hashlib
import mongoengine
import settings


def connect_db():
    mongoengine.connect(settings.DB_NAME, host=settings.DB_ADDRESS, port=settings.DB_PORT)


def md5(astring):
    return hashlib.md5(astring).hexdigest()


if __name__ == "__main__":
    # print md5('2222')
    pass
