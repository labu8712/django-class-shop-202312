from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render

from orders import forms as order_forms
from orders import models as order_models
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
        product = get_object_or_404(product_models.Product, pk=pk)
        shop_car, _ = order_models.ShopCar.objects.get_or_create(user=request.user)

        detail = form.save(commit=False)
        detail.product = product
        detail.shop_car = shop_car

        try:
            detail.save()
        except IntegrityError:
            messages.error(request, "此產品已經在購物車中了")
        else:
            messages.success(request, "加入購物車成功")

        return redirect("products:product_list")

    messages.error(request, f"加入購物車失敗：{form.errors}")
    return redirect("products:product_retrieve", pk=pk)
