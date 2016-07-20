# -*- coding: utf-8 -*-
from canteen import models


def get_canteen(canteen_id):
    canteen = models.Canteen.objects.get(id=canteen_id)
    return canteen


def get_staff_list():
    staff_list = models.Staff.objects.all()
    return staff_list


def create_staff(name="", password="", canteen_id=''):
    staff = models.Staff(name=name, password=password, canteen_id=canteen_id)
    staff.save()
    return staff


def get_staff(staff_id):
    staff = models.Staff.objects.get(id=staff_id)
    return staff


def update_staff(staff_id, **kwargs):
    staff = get_staff(staff_id)
    for key, value in kwargs.iteritems():
        staff[key] = value
    staff.save()
    return staff
