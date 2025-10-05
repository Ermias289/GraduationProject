# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    model = User
    fieldsets = DjangoUserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
