from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from users.models import User

client = APIClient()


class SignupTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email="test@email.com",
            password="test1234",
            name="test",
            phone_number="010-1234-1234"
        )
    
    def tearDown(self):
        User.objects.all().delete()

    def test_success_signup(self):
        url = '/dj-rest-auth/registration/'
        data = {
                "email":"test1@email.com",
                "password1":"test1234",
                "password2":"test1234",
                "name":"test1",
                "phone_number":"010-1111-1111"
            }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user']['email'], "test1@email.com")
        
    
    def test_fail_signup_without_body(self):
        url = '/dj-rest-auth/registration/'
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
                                            "email": [
                                                "This field is required."
                                            ],
                                            "password1": [
                                                "This field is required."
                                            ],
                                            "password2": [
                                                "This field is required."
                                            ],
                                            "name": [
                                                "This field is required."
                                            ],
                                            "phone_number": [
                                                "This field is required."
                                            ]
                                        })
    
    def test_fail_signup_validation_error(self):
        url = '/dj-rest-auth/registration/'
        data = {
                "email":"test@email.com",
                "password1":"test",
                "password2":"test",
                "name":"test",
                "phone_number":"010-1234-1234"
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
                                            "email": [
                                                "A user is already registered with this e-mail address."
                                            ],
                                            "password1": [
                                                "Password must be at least 8 characters with at least one letter and one number."
                                            ],
                                            "phone_number": [
                                                "A user is already registered with this Phone number."
                                            ]
                                        })


class LoginTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        signup_url = '/dj-rest-auth/registration/'
        user_data = {
                "email":"test@email.com",
                "password1":"test1234",
                "password2":"test1234",
                "name":"test",
                "phone_number":"010-1234-1234"
            }

        client.post(signup_url, user_data, format='json')

    def tearDown(self):
        User.objects.all().delete()

    def test_success_login(self):
        url = '/dj-rest-auth/login/'
        data = {
                "email":"test@email.com",
                "password":"test1234",
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user']['email'], "test@email.com")
    
    def test_fail_login_with_wrong_password(self):
        url = '/dj-rest-auth/login/'
        data = {
                "email":"test@email.com",
                "password":"wrong",
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
                                            "non_field_errors": [
                                                "Unable to log in with provided credentials."
                                            ]
                                        })


class LogoutTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        signup_url = '/dj-rest-auth/registration/'
        user_data = {
                "email":"test@email.com",
                "password1":"test1234",
                "password2":"test1234",
                "name":"test",
                "phone_number":"010-1234-1234"
            }

        client.post(signup_url, user_data, format='json')

    def tearDown(self):
        User.objects.all().delete()

    def test_success_logout(self):
        login_url = '/dj-rest-auth/login/'
        data = {
                "email":"test@email.com",
                "password":"test1234",
            }
        response = self.client.post(login_url, data, format='json')

        url = '/dj-rest-auth/logout/'
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, {
                                            "detail": "Refresh token was not included in request data."
                                        })
    
    def test_fail_logout(self):
        url = '/dj-rest-auth/logout/'
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, {
                                            "detail": "Refresh token was not included in request data."
                                        })