# -*- coding: utf-8 -*-
from biz import models


def get_foodtype_list():
    foodtype_list = models.FoodType.objects.all()
    return foodtype_list


def create_foodtype(name=''):
    foodtype = models.FoodType(name=name)
    foodtype.save()
    return foodtype


def get_foodtype(foodtype_id):
    foodtype = models.FoodType.objects.get(id=foodtype_id)
    return foodtype


def update_foodtype(foodtype_id, **kwargs):
    foodtype = get_foodtype(foodtype_id)
    for key, value in kwargs.iteritems():
        foodtype[key] = value

    foodtype.save()
    return foodtype
