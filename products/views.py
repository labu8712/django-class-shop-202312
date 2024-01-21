from django.shortcuts import get_object_or_404, render

from products import models as product_models


def product_list(request):
    products = (
        product_models.Product.objects.select_related("category")
        .prefetch_related("tags")
        .order_by("name")
    )
    return render(request, "products/product_list.html", {"products": products})


def product_retrieve(request, pk):
    product = get_object_or_404(product_models.Product, pk=pk)
    return render(request, "products/product_retrieve.html", {"product": product})
