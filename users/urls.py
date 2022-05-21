from django.contrib import admin
from django.urls import path

from users import views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('signup/', views.SignupView.as_view()),
]

#
#     url(r'^rest-auth/', include('rest_auth.urls')),
#     url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
#     url(r'^account/', include('allauth.urls')),
#     url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
# ]
