from django.contrib.auth import get_user_model
from django.db import models

from products import models as product_models

User = get_user_model()


class ShopCar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(product_models.Product, through="ShopCarDetail")


class ShopCarDetail(models.Model):
    shop_car = models.ForeignKey(ShopCar, on_delete=models.CASCADE)
    product = models.ForeignKey(product_models.Product, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = [
            ["shop_car", "product"],
        ]
