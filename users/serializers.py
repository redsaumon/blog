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
        if User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError('이미 가입된 번호 입니다')
        return phone_number


# from rest_framework_jwt.settings import api_settings
# from django.contrib.auth.models import update_last_login
# from django.contrib.auth import authenticate


# JWT 사용을 위한 설정
# JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
# JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


# 로그인
# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=30)
#     password = serializers.CharField(max_length=128, write_only=True)
#     token = serializers.CharField(max_length=255, read_only=True)
#
#     def validate(self, data):
#         username = data.get("username")
#         password = data.get("password", None)
#         # 사용자 아이디와 비밀번호로 로그인 구현(<-> 사용자 아이디 대신 이메일로도 가능)
#         user = authenticate(username=username, password=password)
#
#         if user is None:
#             return {'username': 'None'}
#         try:
#             payload = JWT_PAYLOAD_HANDLER(user)
#             jwt_token = JWT_ENCODE_HANDLER(payload)
#             update_last_login(None, user)
#
#         except User.DoesNotExist:
#             raise serializers.ValidationError(
#                 'User with given username and password does not exist'
#             )
#         return {
#             'username': user.username,
#             'token': jwt_token
#         }