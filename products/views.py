from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from orders import forms as order_forms
from products import models as product_models


def product_list(request):
    products = (
        product_models.Product.objects.select_related("category")
        .prefetch_related("tags")
        .order_by("name")
        .filter(status=product_models.Product.Status.SHOW)
    )
    if category := request.GET.get("category"):
        products = products.filter(category_id=category)

    return render(request, "products/product_list.html", {"products": products})


@login_required
def product_retrieve(request, pk):
    product = get_object_or_404(product_models.Product, pk=pk)
    return render(
        request,
        "products/product_retrieve.html",
        {
            "product": product,
            "add_to_shop_car_form": order_forms.AddToShopCarForm(),
        },
    )


@login_required
def product_add_to_shop_car(request, pk):
    if request.method.lower() != "post":
        return redirect("products:product_retrieve", pk=pk)

    form = order_forms.AddToShopCarForm(request.POST)
    if form.is_valid():
        pass

    ...
