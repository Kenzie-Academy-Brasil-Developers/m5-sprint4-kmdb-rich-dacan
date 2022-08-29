from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Accounts


class CustomAccountsAdmin(UserAdmin):

    readonly_fields = ("last_login", "date_joined", "updated_at")

    fieldsets = (
        ("Credentials", {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_superuser", "is_active", "is_staff")}),
        ("Personal Info", {"fields": ("birthdate", "bio", "is_critic", "updated_at")}),
        ("Important Dates", {"fields": ("date_joined", "last_login")}),
    )

    list_display = (
        "username",
        "first_name",
        "is_active",
        "is_superuser",
        "is_staff",
        "date_joined",
    )


admin.site.register(Accounts, CustomAccountsAdmin)
