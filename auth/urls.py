from auth import views

urlpatterns = [
    (r"/api/v1/members/?", views.MembersHandler),
    (r"/api/v1/members/([0-9a-z]+)/?", views.MemberHandler),
    (r"/api/v1/addresss/?", views.AddresssHandler),
    (r"/api/v1/addresss/([0-9a-z]+)/?", views.AddressHandler),
    (r"/api/v1/comments/?", views.CommentsHandler),
    (r"/api/v1/comments/([0-9a-z]+)/?", views.CommentHandler),
]
