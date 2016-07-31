# -*- coding: utf-8 -*-
import json
import base
from common.paginate import Page
from biz import dao
from biz import enums
from auth import dao as auth_dao
from auth import utils


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
    @utils.authenticated
    def get(self):
        page_num = int(self.get_argument('page_num', 1))
        status = self.get_argument('status', '')
        search_name = self.get_argument('search_name', '')
        search_content = self.get_argument('search_content', '')
        items_per_page = abs(int(self.get_argument('items_per_page', 10)))
        if items_per_page:
            items_per_page = min(items_per_page, 100)
        else:
            items_per_page = 10
        order_by = self.get_argument('order_by', '')
        order_list = dao.get_order_list()
        if status:
            order_list = order_list.filter(status)
        if order_by:
            order_list = order_list.order_by(order_by)
        if search_name and search_content:
            if search_name == 'member_name':
                member = auth_dao.get_member_by_name(search_content)
                if not member:
                    order_list = []
                else:
                    order_list = order_list.filter(member_id=member.oid)

        page = Page(order_list, page=page_num, items_per_page=items_per_page)
        result = []
        for order in page:
            result.append(order.to_json())

        result = {'status_code': 200, 'result': result, 'current_page': page.page, 'items_per_page': page.items_per_page, 'items_count': page.item_count, 'total_page': page.page_count}
        self.write(json.dumps(result))

    def post(self):
        member_id = self.get_argument('member_id')
        cart = dao.get_cart_by_member_id(member_id)
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
    def get(self, order_id):
        order = dao.get_order(order_id)
        result = {'status_code': 200, 'result': order.to_json()}
        self.write(json.dumps(result))

    def put(self, order_id):
        status = int(self.get_argument('status', 1))
        order = dao.update_order(order_id, status=status)
        result = {'status_code': 200, 'result': order.to_json()}
        self.write(json.dumps(result))

    def delete(self, order_id):
        order = dao.update_order(order_id, status=enums.ORDER_STATUS_DELETE)
        result = {'status_code': 200, 'result': order.to_json()}
        self.write(json.dumps(result))


class CombosHandler(base.BaseHandler):
    def get(self):
        combo_list = dao.get_combo_list()
        result = []
        for combo in combo_list:
            result.append(combo.to_json())

        result = {'status_code': 200, 'result': result}
        self.write(json.dumps(result))

    @utils.authenticated
    def post(self):
        food_id_list = self.get_argument('food_id_list', '')
        food_id_list = food_id_list.split('|')
        print food_id_list
        price = self.get_argument('price', 0)
        combo = dao.create_combo(food_id_list=food_id_list, price=price)

        result = {'status_code': 200, 'result': combo.oid}
        self.write(json.dumps(result))


class ComboHandler(base.BaseHandler):
    def get(self, combo_id):
        combo = dao.get_combo(combo_id)
        result = {'status_code': 200, 'result': combo.to_json()}
        self.write(json.dumps(result))

    def put(self, combo_id):
        pass

    def delete(self, combo_id):
        pass
