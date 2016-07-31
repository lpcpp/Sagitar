# -*- coding: utf-8 -*-
import settings
from common.utils import md5
from auth import dao

import functools


def authenticated(method):
    """Decorate methods with this to require that the user be logged in."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        source = self.get_argument('source')
        if source == settings.FROM_APP:
            random_str = self.get_argument('random_str')
            timestamp = self.get_argument('timestamp')
            signature = self.get_argument('signature')
            app_secret = 'helloworld!@#'
            make_signature = md5(random_str + timestamp + app_secret)
            if make_signature != signature:
                self.write('fail')
                return

        if source == settings.FROM_PC:
            member_id = self.get_secure_cookie('member')
            member = dao.get_member(member_id)
            if not member:
                self.write('fail')
                return
        return method(self, *args, **kwargs)
    return wrapper
