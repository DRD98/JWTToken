from .views import UserRegisterView, UserProfileView, CustomTokenObtainPairView
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    # path('login/', TokenObtainPairView.as_view(), name='user_login'),
    path('login/', CustomTokenObtainPairView.as_view(), name='user_login'),
    path('refresh/', TokenRefreshView.as_view(), name = 'token_refresh'),
    path('register/', UserRegisterView.as_view(), name = 'user_register'),
    path('profile/', UserProfileView.as_view(), name = 'user_profile'),
]
