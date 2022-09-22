from django.urls import path
from clientauth import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/gettoken/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('api/refreshtoken/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('api/verifytoken/', views.ver, name ='token_verify'),
    # path('api/verifytoken/', jwt_views.TokenVerifyView.as_view(), name ='token'),
    # path('api/register/', views.register, name = 'register'),
    # path('api/login/', views.login, name = 'login'),
]
