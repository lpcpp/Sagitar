# -*- coding: utf-8 -*-

import json
import base
from canteen import dao
from canteen import enums


class CanteenHandler(base.BaseHandler):
    def get(self, canteen_id):
        canteen = dao.get_canteen(canteen_id)
        result = {'status_code': 200, 'result': canteen.to_json()}
        self.write(json.dumps(result))


class StaffsHandler(base.BaseHandler):
    def get(self):
        staff_list = dao.get_staff_list()
        result = []
        for staff in staff_list:
            result.append(staff.to_json())
        result = {'status_code': 200, 'result': result}
        self.write(json.dumps(result))

    def post(self):
        name = self.get_argument('name')
        password = self.get_argument('password')
        canteen_id = self.get_argument('canteen_id')
        staff = dao.create_staff(name=name, password=password, canteen_id=canteen_id)
        result = {'status_code': 200, 'result': staff.canteen_id}
        self.write(json.dumps(result))


class StaffHandler(base.BaseHandler):
    def get(self, staff_id):
        staff = dao.get_staff(staff_id)
        result = {'status_code': 200, 'result': staff.to_json()}
        self.write(json.dumps(result))

    def put(self, staff_id):
        name = self.get_argument('name')
        password = self.get_argument("password")
        staff = dao.update_staff(staff_id, name=name, password=password)
        result = {'status_code': 200, 'result': staff.to_json()}
        self.write(json.dumps(result))

    def delete(self, staff_id):
        dao.update_staff(staff_id, status=enums.STAFF_STATUS_UNORMAL)
        result = {'status_code': 200, 'result': []}
        self.write(json.dumps(result))
