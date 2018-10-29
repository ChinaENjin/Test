
from django.conf.urls import url

from message import message_handler, comments_handler

"""
第一种首页配置url(r"^index/$", index_handle.index_handle), 采用一级路由
第二种首页配置url(r'^$',RedirectView.as_view(url= "books/index")), 采用二级路由重定向路径
"""
app_name = "message"
urlpatterns = [
    url(r'^art/(?P<art_pk>[0-9]+)/$',comments_handler.art_comment,name="art_comment"),
    url(r"^$", message_handler.MessageSubmitHandlerV2, name='msg_form'),
]
