from django.urls import path

from products import views as product_views

app_name = "products"

urlpatterns = [
    path("products/", product_views.product_list, name="product_list"),
]
