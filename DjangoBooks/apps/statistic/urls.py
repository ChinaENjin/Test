
from django.conf.urls import url, include
from statistic import shtml_handler,highcharts_handler
"""
第一种首页配置url(r"^index/$", index_handle.index_handle), 采用一级路由
第二种首页配置url(r'^$',RedirectView.as_view(url= "books/index")), 采用二级路由重定向路径
"""
urlpatterns = [
    url(r'^index/$',shtml_handler.IndexHandler),
    url(r'^histogram/', highcharts_handler.HistogramHandler),
]
