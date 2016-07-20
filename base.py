# -*- coding: utf-8 -*-

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        user = self.get_cookie('user')
        if user:
            return user

    def check_xsrf_cookie(self):
        return


class Model(object):
    @property
    def oid(self):
        return str(self.id)
