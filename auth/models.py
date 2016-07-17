# -*- coding: utf-8 -*-
import mongoengine as models
from datetime import datetime
from auth import enums


class Member(models.Document):
    name = models.StringField(max_length=20, required=False)  # 姓名
    password = models.StringField(required=True)  # 登陆密码
    age = models.IntField(required=False)    # 年龄
    sex = models.IntField(choices=enums.SEX_LIST, required=False)  # 性别
    mobile = models.StringField(required=False)    # 电话
    create_time = models.DateTimeField(default=datetime.now)  # 创建时间
    status = models.IntField(choices=enums.MEMBER_STATUS_LIST, default=enums.MEMBER_STATUS_NORMAL, required=True)  # 用户状态
    custom_attr = models.DictField()    # 定制属性

    @property
    def oid(self):
        return str(self.id)

    meta = {
        'indexes': ['mobile', 'name']
    }


class Address(models.Document):
    member_id = models.StringField()
    content = models.StringField()

    @property
    def oid(self):
        return str(self.id)


class Comment(models.Document):
    member_id = models.StringField()
    create_time = models.DateTimeField(default=datetime.now)
    content = models.StringField(min_length=10, max_length=200)
    star = models.IntField()  # 从0星到5星
    status = models.IntField(choices=enums.COMMENT_STATUS_LIST, default=enums.COMMENT_STATUS_NORMAL, required=True)  # 用户状态
