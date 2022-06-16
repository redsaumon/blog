from turtle import title
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User
from api.models import Post, Category

client = APIClient()


class PostTests(APITestCase):
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

        cls.user = User.objects.last()

        cls.category = Category.objects.create(
            name='IT'
        )

        Post.objects.bulk_create([
            Post(title='title1', description='description1', content='content1', user_id=1, category_id=1),
            Post(title='title2', description='description2', content='content2', user_id=1, category_id=1),
            Post(title='title3', description='description3', content='content3', user_id=1, category_id=1),
            Post(title='title4', description='description4', content='content4', user_id=1, category_id=1),
            Post(title='title5', description='description5', content='content5', user_id=1, category_id=1),
            Post(title='title6', description='description6', content='content6', user_id=1, category_id=1),
            ])
    
    def tearDown(self):
        Post.objects.all().delete()
        Category.objects.all().delete()
        User.objects.all().delete()

    def test_success_post_create(self):
        url = '/api/post/'
        data = {
                "category": self.category.name,
                "title":"test",
                "description":"test",
                "content":"test"
            }
        user = User.objects.last()
        refresh = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_fail_post_create_without_login(self):
        url = '/api/post/'
        data = {
                "category": self.category.name,
                "title":"test",
                "description":"test",
                "content":"test"
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {
                                            "detail": "Authentication credentials were not provided."
                                        })

    def test_fail_post_create_without_body(self):
        url = '/api/post/'
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
                                            "category": [
                                                "This field is required."
                                            ],
                                            "title": [
                                                "This field is required."
                                            ],
                                            "content": [
                                                "This field is required."
                                            ]
                                        })
    
    def test_success_post_list(self):
        url = '/api/posts/'
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_success_post_list_with_pagination(self):
        url = '/api/posts/?page=2'
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['curPage'], 2)
    
    def test_success_post_retrieve(self):
        url = '/api/posts/1/'
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_fail_post_retrieve_nonexistent_post(self):
        url = '/api/posts/99999/'
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_success_post_like(self):
        url = '/api/posts/1/like/'
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 1)
    
    def test_fail_post_like_nonexistent_post(self):
        url = '/api/posts/99999/like/'
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_success_post_delete(self):
        url = '/api/posts/1/'
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_fail_post_delete_without_login(self):
        url = '/api/posts/1/'
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_fail_post_delete_nonexistent_post(self):
        url = '/api/posts/99999/'
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    