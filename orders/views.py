from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

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
