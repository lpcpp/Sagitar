# -*- coding: utf-8 -*-
from base import Model
import mongoengine as models


class Canteen(Model, models.Document):
    name = models.StringField()


class Staff(Model, models.Document):
    name = models.StringField()
    password = models.StringField()
    canteen_id = models.StringField()
    status = models.IntField()
