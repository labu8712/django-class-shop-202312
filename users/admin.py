from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from users import models as user_models


@admin.register(user_models.User)
class UserAdmin(DjangoUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
    )
