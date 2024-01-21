from django.urls import path

from orders import views as orders_views

app_name = "orders"

urlpatterns = [
    path("shop-car/detail/", orders_views.shop_car_detail, name="shop_car_detail"),
    path("buy/", orders_views.buy, name="buy"),
]
