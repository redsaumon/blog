from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(UserAdmin):
    list_display = ('email', 'name', 'phone_number', 'last_login',)
    ordering = ('email',)

admin.site.register(User, UserAdmin)