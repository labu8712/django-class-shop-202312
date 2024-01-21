from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from orders import models as order_models


@login_required
def shop_car_detail(request):
    shop_car = get_object_or_404(
        order_models.ShopCar,
        user=request.user,
    )

    total_price = 0
    products = []
    for detail in shop_car.shopcardetail_set.all():
        price = detail.product.price * detail.count
        products.append([detail.product, price])
        total_price += price

    return render(
        request,
        "orders/shop_car_detail.html",
        {"products": products, "total_price": total_price},
    )


@login_required
def buy(request):
    if request.method.lower() != "post":
        return redirect("orders:shop_car_detail")

    shop_car = get_object_or_404(
        order_models.ShopCar,
        user=request.user,
    )

    order = order_models.Order.objects.create(user=request.user)

    order_details = []
    for detail in shop_car.shopcardetail_set.all():
        detail = order_models.OrderDetail(
            order=order,
            product=detail.product,
            count=detail.count,
            price=detail.product.price,
        )
        order_details.append(detail)

    order_models.OrderDetail.objects.bulk_create(order_details)
    order_models.ShopCarDetail.objects.filter(shop_car=shop_car).delete()

    messages.success(request, "下單成功")
    return redirect("products:product_list")
