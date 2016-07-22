import json
from base import BaseHandler
from biz import dao


class CartHandler(BaseHandler):
    def get(self):
        member_id = self.get_argument('member_id')
        cart = dao.get_cart_by_member_id(member_id)
        fooditem_list = dao.get_fooditem_list(cart.get('food_item_id_list', []))
        comboitem_list = dao.get_comboitem_list(cart.get('combo_item_id_list', []))
        fooditem_json_list = []
        comboitem_json_list = []
        for fooditem in fooditem_list:
            fooditem_json_list.append(fooditem.to_json())
        for comboitem in comboitem_list:
            comboitem_json_list.append(comboitem.to_json())

        result = {'fooditem_list': fooditem_json_list, 'comboitem_list': comboitem_json_list}

        self.write(json.dumps({'status_code': 200, 'result': result}))
        return

    def put(self):
        fooditem_id = self.get_arguemnt('fooditem_id')
        comboitem_id = self.get_arguemnt('comboitem_id')
        cart = dao.update_cart(fooditem_id=fooditem_id, comboitem_id=comboitem_id)
        self.write(json.dumps(cart.to_json()))
