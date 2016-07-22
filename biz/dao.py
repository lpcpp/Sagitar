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


def get_food_list():
    food_list = models.Food.objects.all()
    return food_list


def create_food(foodtype_id="", name="", price=""):
    print 111, name
    food = models.Food(foodtype_id=foodtype_id, name=name, price=price)
    food.save()
    return food


def get_food(food_id):
    food = models.Food.objects.get(id=food_id)
    return food


def update_food(food_id, **kwargs):
    food = get_food(food_id)
    for key, value in kwargs.iteritems():
        if value:
            food[key] = value
    food.save()
    return food
