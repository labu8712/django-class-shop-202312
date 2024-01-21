from django.contrib import admin

from products import models as product_models


@admin.register(product_models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "status")
    list_filter = ("status",)


@admin.register(product_models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(product_models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "status")
    list_filter = ("status", "category", "tags")
    filter_horizontal = ("tags",)
