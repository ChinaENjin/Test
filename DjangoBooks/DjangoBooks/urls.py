
from django.conf.urls import url, include
# from django.contrib import admin
from django.views.generic import RedirectView
from books.index_handle import index_handle

import xadmin
"""
第一种首页配置url(r"^index/$", index_handle.index_handle), 采用一级路由
第二种首页配置url(r'^$',RedirectView.as_view(url= "books/index")), 采用二级路由重定向路径
"""
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^$',index_handle),
    url(r'^xadmin/',xadmin.site.urls),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
    url(r'^$',RedirectView.as_view(url= "books/index")),
    url(r'^books/',include('books.urls')),
    url(r'^user/',include('user_center.urls')),
    url(r'^message/',include('message.urls')),
    url(r'^apis/', include("drf_apis.urls")),
    url(r'^statistic/',include('statistic.urls')),
    url(r'^cart/',include('commerce.urls')),
]
