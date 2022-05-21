import re

from rest_framework import serializers
from allauth.account.adapter import DefaultAccountAdapter


class CustomUserAdapter(DefaultAccountAdapter):
    def clean_password(self, password, user=None):
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password):
            raise serializers.ValidationError(
                {'password': ['Password must be at least 8 characters with at least one letter and one number']})
        return password

    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)

        user.name = request.data.get('name', '')
        user.phone_number = request.data.get('phone_number', '')

        user.save()
        return user