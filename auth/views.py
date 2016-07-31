# -*- coding: utf-8 -*-

import json
import base
from auth import dao
from auth import utils
from auth import enums


class MembersHandler(base.BaseHandler):
    def get(self):
        member_list = dao.get_member_list()
        result = []
        for member in member_list:
            result.append(member.to_json())
        result = {'status_code': 200, 'result': result}
        self.write(json.dumps(result))

    def post(self):
        name = self.get_argument('name')
        password = self.get_argument('password')
        sex = int(self.get_argument('sex', 3))
        age = int(self.get_argument('age'))
        mobile = self.get_argument('mobile')
        member = dao.create_member(name=name, password=password, sex=sex, age=age, mobile=mobile)
        result = {'status_code': 200, 'result': member.oid}
        self.write(json.dumps(result))


class MemberHandler(base.BaseHandler):
    def get(self, member_id):
        member = dao.get_member(member_id)
        self.set_secure_cookie('member_id', member.oid)
        result = {'status_code': 200, 'result': member.to_json()}
        self.write(json.dumps(result))

    @utils.authenticated
    def put(self, member_id, aa=11):
        mobile = self.get_argument('mobile')
        member = dao.update_member(member_id, mobile=mobile)
        result = {'status_code': 200, 'result': member.to_json()}
        self.write(json.dumps(result))

    def delete(self, member_id):
        dao.update_member(member_id, status=enums.MEMBER_STATUS_UNORMAL)
        result = {'status_code': 200, 'result': []}
        self.write(json.dumps(result))


class AddresssHandler(base.BaseHandler):
    def get(self):
        address_list = dao.get_address_list()
        result = []
        for address in address_list:
            result.append(address.to_json())
        result = {'status_code': 200, 'result': result}
        self.write(json.dumps(result))

    def post(self):
        content = self.get_argument('content')
        member_id = self.get_argument('member_id')
        address = dao.create_address(member_id=member_id, content=content)
        result = {'status_code': 200, 'result': address.oid}
        self.write(json.dumps(result))


class AddressHandler(base.BaseHandler):
    def get(self, address_id):
        address = dao.get_address(address_id)
        result = {'status_code': 200, 'result': address.to_json()}
        self.write(json.dumps(result))

    def put(self, address_id):
        content = self.get_argument('content')
        address = dao.update_address(address_id, content=content)
        result = {'status_code': 200, 'result': address.to_json()}
        self.write(json.dumps(result))

    def delete(self, address_id):
        dao.update_address(address_id, status=enums.ADDRESS_STATUS_DELETE)
        result = {'status_code': 200, 'result': []}
        self.write(json.dumps(result))


class CommentsHandler(base.BaseHandler):
    def get(self):
        comment_list = dao.get_comment_list()
        result = []
        for comment in comment_list:
            result.append(comment.to_json())
        result = {'status_code': 200, 'result': result}
        self.write(json.dumps(result))

    def post(self):
        member_id = self.get_argument('member_id')
        content = self.get_argument('content')
        star = self.get_argument('star')
        star = dao.create_address(member_id=member_id, content=content, star=star)
        result = {'status_code': 200, 'result': star.oid}
        self.write(json.dumps(result))


class CommentHandler(base.BaseHandler):
    def get(self, comment_id):
        comment = dao.get_comment(comment_id)
        result = {'status_code': 200, 'result': comment.to_json()}
        self.write(json.dumps(result))

    def delete(self, comment_id):
        dao.update_comment(comment_id, status=enums.COMMENT_STATUS_DELETE)
        result = {'status_code': 200, 'result': []}
        self.write(json.dumps(result))
