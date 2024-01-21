from django.shortcuts import render

from products import models as product_models


def product_list(request):
    products = (
        product_models.Product.objects.select_related("category")
        .prefetch_related("tags")
        .order_by("name")
    )
    return render(request, "products/product_list.html", {"products": products})
