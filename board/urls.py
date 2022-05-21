from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('api/', include('api.urls')),
    # api에서 로그인할 수 있도록 해줌. 추후 permission과 auth기능 추가시 사용
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]