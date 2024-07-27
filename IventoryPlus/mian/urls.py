from django.urls import path
from . import views

app_name = "mian"

urlpatterns = [
    path("", views.home, name="home"),
    path('product/pay/<product_id>/' , views.pay_product , name="pay_product"),
]