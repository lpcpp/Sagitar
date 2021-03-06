# -*- coding: utf-8 -*-
FOODTYPE_STATUS_NORMAL = 1
FOODTYPE_STATUS_DELETED = 2


FOOD_STATUS_NORMAL = 1
FOOD_STATUS_DELETED = 2


ORDER_STATUS_CREATE = 1     # 刚创建的订单，没有确认的。
ORDER_STATUS_CONFIRM = 2    # 用户确认的订单，就是真正需要显示给厨房的。
ORDER_STATUS_PAID = 3       # 用户已经支付完成的订单
ORDER_STATUS_CANCEL = 4     # 用户取消的订单
ORDER_STATUS_OUTDATE = 5    # 过期的订单, 用户创建之后就不管了。
ORDER_STATUS_DELETE = 6     # 删除的订单


ORDER_STATUS_LIST = [ORDER_STATUS_CREATE, ORDER_STATUS_CONFIRM, ORDER_STATUS_PAID, ORDER_STATUS_CANCEL, ORDER_STATUS_OUTDATE, ORDER_STATUS_DELETE]
