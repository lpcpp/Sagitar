# -*- coding: utf-8 -*-
import mongoengine as models


class Canteen(models.Document):
    name = models.StringField()


class Staff(models.Document):
    name = models.StringField()
    password = models.StringField()
    canteen_id = models.StringField()
