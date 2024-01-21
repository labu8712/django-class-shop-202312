from django import forms

from orders import models as order_models


class AddToShopCarForm(forms.ModelForm):
    class Meta:
        model = order_models.ShopCarDetail
        fields = ("count",)
