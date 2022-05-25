import re

from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone_number']


class CustomRegisterSerializer(RegisterSerializer):
    username = None
    name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)

    def get_clean_data(self):
        data = super().get_cleaned_data()
        data['name'] = self.validated_data.get('name', '')
        data['phone_number'] = self.validated_data.get('phone_number', '')
        return data

    def validate_phone_number(self, phone_number):
        if not re.match(r'\d{2,3}-\d{3,4}-\d{4}', phone_number):
            raise serializers.ValidationError('Phone number formatted incorrectly.')

        if User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError('A user is already registered with this Phone number.')
        return phone_number