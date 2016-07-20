# -*- coding: utf-8 -*-
import index
import auth.urls
import canteen.urls
import biz.urls


urlpatterns = [
    (r"/?", index.IndexHandler),
]


urlpatterns += auth.urls.urlpatterns + canteen.urls.urlpatterns + biz.urls.urlpatterns
