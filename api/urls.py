from django.urls import path, include
from rest_framework import routers

from api import views


router = routers.DefaultRouter()
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', views.PostListAPIView.as_view(), name='post-list'),
    path('post/', views.PostCreateAPIView.as_view(), name='post-create'),
    path('posts/<int:pk>/', views.PostRetrieveAPIView.as_view(), name='post-detail'),
    path('posts/<int:pk>/like/', views.PostLikeAPIView.as_view(), name='post-like'),
    path('catetags/', views.CateTagAPIView.as_view(), name='catetag'),
]