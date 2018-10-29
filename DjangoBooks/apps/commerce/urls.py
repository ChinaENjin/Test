
from django.conf.urls import url
from commerce.cart_handler import ViewCartHandler, AddCartHandler,CleanCartHandler,CartOrderHandler,OrderSubmitHandler
urlpatterns = [
    url(r'^view/$',ViewCartHandler),
    url(r'^add/$',AddCartHandler),
    url(r'^clean/$',CleanCartHandler),
    url(r'^order/$',CartOrderHandler),
    url(r'^submit_order/$',OrderSubmitHandler, name="product_order"),

]
