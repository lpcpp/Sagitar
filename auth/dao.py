# -*- coding: utf-8 -*-
from auth import models


def get_member_list():
    member_list = models.Member.objects.all()
    return member_list


def create_member(name='', password='', sex='', age=0, mobile=''):
    member = models.Member(
        name=name,
        password=password,
        sex=sex,
        age=age,
        mobile=mobile
    )
    member.save()
    return member


def get_member(member_id):
    member = models.Member.objects.get(id=member_id)
    return member


def update_member(member_id, **kwargs):
    member = get_member(member_id)
    for key, value in kwargs.iteritems():
        member[key] = value

    member.save()
    return member


def get_address_list():
    address_list = models.Address.objects.all()
    return address_list


def create_address(member_id, content=''):
    address = models.Address(member_id, content=content)
    address.save()
    return address


def get_address(address_id):
    address = models.Address.objects.get(id=address_id)
    return address


def update_address(address_id, **kwargs):
    address = get_address(address_id)
    for key, value in kwargs.iteritems():
        address[key] = value

    address.save()
    return address


def get_comment_list():
    comment_list = models.Comment.objects.all()
    return comment_list


def create_comment(member_id, content='', star=''):
    comment = models.Address(member_id, content=content, star=star)
    comment.save()
    return comment


def get_comment(comment_id):
    comment = models.Comment.objects.get(id=comment_id)
    return comment


def update_comment(comment_id, **kwargs):
    comment = get_address(comment_id)
    for key, value in kwargs.iteritems():
        comment[key] = value

    comment.save()
    return comment
