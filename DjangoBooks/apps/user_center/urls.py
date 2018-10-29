
from django.conf.urls import url
from user_center import register_handler,login_handler,activatehandler

urlpatterns = [
    url(r'^register/$',register_handler.Register_handle,name= 'user_register'),
    url(r"^login/$",login_handler.Login_handler,name='user_login'),
    url(r'^logout/$',login_handler.LogoutHandler),
    url(r'^active/$',activatehandler.ActivateHandler),
]
