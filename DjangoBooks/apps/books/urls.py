
from django.conf.urls import url
from books import index_handle,add_handler,detail_handler,art_capter_handler,search_handler

app_name = "books"
urlpatterns = [
    url(r"^index/$", index_handle.index_handle),
    # url(r"^add/$",add_handler.AddHandler),
    url(r"^detail/$",detail_handler.detail_handler),
    url(r'^capter/$',art_capter_handler.ArtCapterHandler),
    url(r'^search/$',search_handler.search_handler),
]
