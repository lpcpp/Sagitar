from biz import views

urlpatterns = [
    (r"/api/v1/foodtypes/?", views.FoodTypesHandler),
    (r"/api/v1/foodtypes/([0-9a-z]+)/?", views.FoodTypeHandler),
    (r"/api/v1/foods/?", views.FoodsHandler),
    (r"/api/v1/foods/([0-9a-z]+)/?", views.FoodHandler),
]
