from .views import UserRegisterView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


urlpatterns = [
   path('login/', TokenObtainPairView.as_view(), name='user_login'),
   path('register/', UserRegisterView.as_view(), name = 'user_register'),
]
