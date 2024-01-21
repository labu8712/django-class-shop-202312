from django.urls import path

from products import views as product_views

app_name = "products"

urlpatterns = [
    path("products/", product_views.product_list, name="product_list"),
    path("products/<int:pk>/", product_views.product_retrieve, name="product_retrieve"),
    path(
        "products/<int:pk>/add-to-shop-car/",
        product_views.product_add_to_shop_car,
        name="product_add_to_shop_car",
    ),
]
