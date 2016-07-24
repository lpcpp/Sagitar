import json
from base import BaseHandler
from biz import dao


class CartHandler(BaseHandler):
    def get(self):
        member_id = self.get_argument('member_id')
        cart = dao.get_cart_by_member_id(member_id)
        if cart:
            cart = eval(cart)
        foods_dict = cart.get('food_id_list', {})
        combo_list = dao.get_combo_list_by_id_list(cart.get('combo_id_list', {}))
        food_json_list = []
        combo_json_list = []
        for food_id, food_num in foods_dict.iteritems():
            food = dao.get_food(food_id)
            food_json_list.append((food.to_json(), food_num))

        for combo in combo_list:
            combo_json_list.append(combo.to_json())

        result = {'food_list': food_json_list, 'combo_list': combo_json_list}

        self.write({'status_code': 200, 'result': result})
        return

    def put(self):
        member_id = self.get_argument('member_id')
        food_id = self.get_argument('food_id', '')
        combo_id = self.get_argument('combo_id', '')
        cart = dao.update_cart(member_id=member_id, food_id=food_id, combo_id=combo_id)
        self.write(json.dumps(cart))
