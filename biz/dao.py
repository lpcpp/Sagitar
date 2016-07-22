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


def get_cart_by_member_id(member_id):
    """
    cart = redis.get(member_id)
    return cart
    """


def get_fooditem(fooditem_id):
    try:
        fooditem = models.FoodItem.objects.get(id=fooditem_id)
    except:
        fooditem = None

    return fooditem


def get_fooditem_list(fooditem_id_list):
    fooditem_list = []
    for fooditem_id in fooditem_id_list:
        fooditem = get_fooditem(fooditem_id)
        fooditem_list.append(fooditem)

    return fooditem_list


def get_comboitem(comboitem_id):
    try:
        comboitem = models.ComboItem.objects.get(id=comboitem_id)
    except:
        comboitem = None

    return comboitem


def get_comboitem_list(comboitem_id_list):
    comboitem_list = []
    for comboitem_id in comboitem_id_list:
        comboitem = get_comboitem(comboitem_id)
        comboitem_list.append(comboitem)

    return comboitem_list


def update_cart(fooditem_id, comboitem_id):
    cart = get_cart_by_member_id(member_id)
    if fooditem_id:
        if fooditem_id in cart.get('fooditem_id_list'):
            cart.fooditem_id_list[fooditem_id] += 1
        else:
            cart.fooditem_id_list[fooditem_id] = 1

    if comboitem_id:
        if comboitem_id in cart.get('comboitem_id_list'):
            cart.comboitem_id_list[comboitem_id] += 1
        else:
            cart.comboitem_id_list[comboitem_id] = 1

    return cart
