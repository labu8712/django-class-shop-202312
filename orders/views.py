from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from orders import models as order_models


@login_required
def shop_car_detail(request):
    shop_car = get_object_or_404(
        order_models.ShopCar,
        user=request.user,
    )
    return render(request, "orders/shop_car_detail.html", {"shop_car": shop_car})
