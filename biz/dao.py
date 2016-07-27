# -*- coding: utf-8 -*-
from biz import models
from common.utils import connect_redis


redis_conn = connect_redis()


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


def get_food(food_id):
    food = models.Food.objects.get(id=food_id)
    return food


def get_food_list_by_id_list(food_id_list):
    food_list = []
    for food_id in food_id_list:
        food = get_food(food_id)
        food_list.append(food)

    return food_list


def get_combo(combo_id):
    combo = models.Combo.objects.get(id=combo_id)
    return combo


def get_combo_list_by_id_list(combo_id_list):
    combo_list = []
    for combo_id in combo_id_list:
        combo = get_combo(combo_id)
        combo_list.append(combo)

    return combo_list


def create_food(foodtype_id="", name="", price=""):
    food = models.Food(foodtype_id=foodtype_id, name=name, price=price)
    food.save()
    return food


def update_food(food_id, **kwargs):
    food = get_food(food_id)
    for key, value in kwargs.iteritems():
        if value:
            food[key] = value
    food.save()
    return food


def get_cart_by_member_id(member_id):
    cart = redis_conn.get(member_id)
    if not cart:
        return {}
    return cart


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


def redis_set(key, value):
    redis_conn.set(key, value)


def update_cart(member_id, food_id, combo_id):
    cart = get_cart_by_member_id(member_id)
    if cart:
        cart = eval(cart)
    else:
        cart = {'food_id_list': {}, 'combo_id_list': {}}

    if food_id:
        if food_id in cart.get('food_id_list', []):
            cart['food_id_list'][food_id] += 1
        else:
            cart['food_id_list'][food_id] = 1

    if combo_id:
        print cart
        if combo_id in cart.get('combo_id_list', {}):
            cart['combo_id_list'][combo_id] += 1
        else:
            cart['combo_id_list'][combo_id] = 1

    redis_set(member_id, cart)
    return cart


def create_fooditem(food_id='', num=''):
    fooditem = models.FoodItem(food_id=food_id, num=num)
    fooditem.save()
    return fooditem


def create_order(food_item_list=[], combo_id_list=[], member_id='', address=''):
    order = models.Order(food_item_list=food_item_list, combo_id_list=combo_id_list, member_id=member_id, address=address)
    order.save()
    return order


def clean_cart(member_id):
    redis_set(member_id, {})


def create_combo(food_id_list='', price=''):
    combo = models.Combo(food_id_list=food_id_list, price=price)
    combo.save()

    return combo


def get_combo_list():
    combo_list = models.Combo.objects.all()
    return combo_list


def get_order_list():
    order_list = models.Order.objects.all()
    return order_list


def get_order(order_id):
    order = models.Order.objects.get(id=order_id)
    return order


def update_order(order_id, **kwargs):
    order = get_order(order_id)
    for key, value in kwargs.iteritems():
        if value:
            order[key] = value
    order.save()
    return order
