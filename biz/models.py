# -*- coding: utf-8 -*-
import mongoengine as models
from base import Model
from datetime import datetime
from biz import enums


class FoodType(Model, models.Document):
    name = models.StringField()
    create_time = models.DateTimeField(default=datetime.now)
    status = models.IntField(default=enums.FOODTYPE_STATUS_NORMAL)


class Food(Model, models.Document):
    foodtype_id = models.StringField()
    name = models.StringField()
    price = models.FloatField()
    create_time = models.DateTimeField(default=datetime.now)
    status = models.IntField(default=enums.FOOD_STATUS_NORMAL)


class FoodItem(Model, models.Document):
    food_id = models.StringField()
    num = models.IntField(default=0)


class Combo(Model, models.Document):  # 套餐
    food_id_list = models.ListField()
    price = models.FloatField()
    create_time = models.DateTimeField(default=datetime.now)
    status = models.IntField()


class ComboItem(Model, models.Document):
    combo_id = models.StringField()
    num = models.IntField()


class Order(models.Document):
    food_item_list = models.ListField()
    combo_id_list = models.ListField()
    create_time = models.DateTimeField(default=datetime.now)
    member_id = models.StringField()
    address = models.StringField()
    actual_cost = models.FloatField()   # 实际消费
    benefit = models.FloatField()       # 优惠
    status = models.IntField(default=enums.ORDER_STATUS_CREATE, choices=enums.ORDER_STATUS_LIST)
