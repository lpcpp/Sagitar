# -*- coding: utf-8 -*-
from biz import views
from biz import ajax

urlpatterns = [
    (r"/api/v1/foodtypes/?", views.FoodTypesHandler),
    (r"/api/v1/foodtypes/([0-9a-z]+)/?", views.FoodTypeHandler),
    (r"/api/v1/foods/?", views.FoodsHandler),
    (r"/api/v1/foods/([0-9a-z]+)/?", views.FoodHandler),
    (r"/api/v1/orders/?", views.OrdersHandler),
    (r"/api/v1/orders/([0-9a-z]+)/?", views.OrderHandler),

    (r"/ajax/cart/?", ajax.CartHandler),
]
