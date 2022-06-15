from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class SignupTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email="test@email.com",
            password="test1234",
            name="test",
            phone_number="010-1234-1234"
        )

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
        self.assertEqual(User.objects.last().email, "test1@email.com")
    
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