from django.urls import path, include
# from clientauth import views
# from rest_framework_simplejwt import views as jwt_views

urlpatterns = [ path('user/', include('clientauth.urls'), name = 'redirection'), ]