from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    #path('stud/gettoken/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('stud/login/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    #path('stud/refreshtoken/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    # path('stud/refreshtoken/', jwt_views.TokenRefreshView.as_view()),
    # path('stud/verifytoken/', views.ver, name ='token_verify'),
    # path('stud/verifytoken/', jwt_views.TokenVerifyView.as_view(), name ='token'),
    path('stud/register/', views.register, name = 'register'),
]
