# -*- coding: utf-8 -*-
import mongoengine as models


class Admin(models.Document):
    name = models.StringField(require=True)
    password = models.StringField(require=True)
    group_id = models.StringField(require=True)


class Group(models.Document):
    name = models.StringField(require=True)
    perm_list = models.StringField()


class Perm(models.Document):
    name = models.StringField()
