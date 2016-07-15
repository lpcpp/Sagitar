# -*- coding: utf-8 -*-
import mongonengine as models
from datetime import datetime


class FoodType(models.Document):
    name = models.StringField()


class Food(models.Document):
    food_type = models.StringField()
    name = models.StringField()
    price = models.FloatField()
    create_time = models.DateTimeField(default=datetime.now)


class FoodItem(models.Document):
    food_id = models.StringField()
    num = models.IntField()


class Combo(models.Document):  # 套餐
    food_item_list = models.ListField()
    price = models.FloatField()


class ComboItem(models.Document):
    combo_id = models.StringField()
    num = models.IntField()


class Order(models.Document):
    food_item_list = models.ListField()
    combo_id = models.StringField()
    create_time = models.DateTimeField()
    member_id = models.StringField()
    address = models.StringField()
    actual_cost = models.FloatField()   # 实际消费
    benefit = models.FloatField()       # 优惠
