from canteen import views

urlpatterns = [
    (r"/api/v1/canteens/([0-9a-z]+)/?", views.CanteenHandler),
    (r"/api/v1/staffs/?", views.StaffsHandler),
    (r"/api/v1/staffs/([0-9a-z]+)/?", views.StaffHandler),
]
