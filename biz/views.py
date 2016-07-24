# -*- coding: utf-8 -*-
import json
import base
from biz import dao
from biz import enums


class FoodTypesHandler(base.BaseHandler):
    def get(self):
        foodtype_list = dao.get_foodtype_list()
        result = []
        for foodtype in foodtype_list:
            result.append(foodtype.to_json())

        result = {'status_code': 200, 'result': result}
        self.write(json.dumps(result))

    def post(self):
        name = self.get_argument('name', '')
        foodtype = dao.create_foodtype(name=name)

        result = {'status_code': 200, 'result': foodtype.oid}
        self.write(json.dumps(result))


class FoodTypeHandler(base.BaseHandler):
    def get(self, foodtype_id):
        foodtype = dao.get_foodtype()
        result = {'status_code': 200, 'result': foodtype.to_json()}
        self.write(json.dumps(result))

    def put(self, foodtype_id):
        name = self.get_argument('name', '')
        foodtype = dao.update_foodtype(foodtype_id, name=name)

        result = {'status_code': 200, 'result': foodtype.oid}
        self.write(json.dumps(result))

    def delete(self, foodtype_id):
        foodtype = dao.update_foodtype(foodtype_id, status=enums.FOODTYPE_STATUS_DELETED)

        result = {'status_code': 200, 'result': foodtype.oid}
        self.write(json.dumps(result))


class FoodsHandler(base.BaseHandler):
    def get(self):
        food_list = dao.get_food_list()
        result = []
        for food in food_list:
            result.append(food.to_json())

        result = {'status_code': 200, 'result': result}
        self.write(json.dumps(result))

    def post(self):
        foodtype_id = self.get_argument('foodtype_id', '')
        name = self.get_argument('name', '')
        price = float(self.get_argument('price', 0))
        food = dao.create_food(foodtype_id=foodtype_id, name=name, price=price)

        result = {'status_code': 200, 'result': food.oid}
        self.write(json.dumps(result))


class FoodHandler(base.BaseHandler):
    def get(self, food_id):
        food = dao.get_food(food_id)
        result = {'status_code': 200, 'result': food.to_json()}
        self.write(json.dumps(result))

    def put(self, food_id):
        name = self.get_argument('name', '')
        price = float(self.get_argument('price', 0))
        food = dao.update_food(food_id, name=name, price=price)

        result = {'status_code': 200, 'result': food.oid}
        self.write(json.dumps(result))

    def delete(self, food_id):
        food = dao.update_food(food_id, status=enums.FOOD_STATUS_DELETED)

        result = {'status_code': 200, 'result': food.oid}
        self.write(json.dumps(result))


class OrdersHandler(base.BaseHandler):
    def get(self):
        order_list = dao.get_order_list()
        result = []
        for order in order_list:
            result.append(order.to_json())

        result = {'status_code': 200, 'result': result}
        self.write(json.dumps(result))

    def post(self):
        member_id = self.get_argument('member_id')
        cart = dao.get_cart_by_member_id(member_id)
        print cart
        if cart:
            cart = eval(cart)

        food_id_list = cart.get('food_id_list', {})
        food_item_list = []
        for food_id, food_num in food_id_list.iteritems():
            fooditem = dao.create_fooditem(food_id=food_id, num=food_num)
            food_item_list.append(fooditem)

        combo_id_list = []
        order = dao.create_order(food_item_list=food_item_list, combo_id_list=combo_id_list, member_id=member_id)
        dao.clean_cart(member_id)
        result = {'status_code': 200, 'result': order.to_json()}
        self.write(result)


class OrderHandler(base.BaseHandler):
    def get(self):
        pass
