from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User
from api.models import Post, Category, Comment


client = APIClient()

class CommentTests(APITestCase):
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
            Post(title='title1', description='description1', content='content1', user_id=cls.user.id, category_id=cls.category.id),
            Post(title='title2', description='description2', content='content2', user_id=cls.user.id, category_id=cls.category.id),
            Post(title='title3', description='description3', content='content3', user_id=cls.user.id, category_id=cls.category.id),
            Post(title='title4', description='description4', content='content4', user_id=cls.user.id, category_id=cls.category.id),
            Post(title='title5', description='description5', content='content5', user_id=cls.user.id, category_id=cls.category.id),
            Post(title='title6', description='description6', content='content6', user_id=cls.user.id, category_id=cls.category.id),
            ])
        
        cls.post = Post.objects.first()

        cls.comment = Comment.objects.create(
            content='test',
            post_id=cls.post.id,
            user_id=cls.user.id
        )
    
    def tearDown(self):
        Post.objects.all().delete()
        Category.objects.all().delete()
        User.objects.all().delete()
        Comment.objects.all().delete()

    def test_success_comment_create(self):
        url = '/api/comments/'
        data = {
                "content": "test",
                "post": self.post.id
            }
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_fail_comment_create_without_login(self):
        url = '/api/comments/'
        data = {
                "content": "test",
                "post": self.post.id
            }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_fail_comment_create_without_body(self):
        url = '/api/comments/'
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.post(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_fail_comment_create_nonexistent_post(self):
        url = '/api/comments/'
        data = {
                "content": "test",
                "post": 99999
            }
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_success_comment_List(self):
        url = '/api/comments/'
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_success_comment_retrieve(self):
        url = f'/api/comments/{self.comment.id}/'
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_fail_comment_retrieve_nonexistent_comment(self):
        url = '/api/comments/99999/'
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_success_comment_update(self):
        url = f'/api/comments/{self.comment.id}/'
        data = {
                "content": "update test",
            }
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], 'update test')
    
    def test_fail_comment_update_without_login(self):
        url = f'/api/comments/{self.comment.id}/'
        data = {
                "content": "update test",
            }
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_fail_comment_update_nonexistent_comment(self):
        url = '/api/comments/99999/'
        data = {
                "content": "update test",
            }
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_fail_comment_update_without_body(self):
        url = f'/api/comments/{self.comment.id}/'
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.put(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_success_comment_delete(self):
        url = f'/api/comments/{self.comment.id}/'
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_fail_comment_delete_without_login(self):
        url = f'/api/comments/{self.comment.id}/'
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_fail_comment_delete_nonexistent_comment(self):
        url = '/api/comments/99999/'
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)