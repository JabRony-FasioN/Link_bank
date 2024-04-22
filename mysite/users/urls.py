from django.urls import path, include

from users.views import Register, ContentVeiw

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
]