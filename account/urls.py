
from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("register/", UserRegisterAPIView.as_view(), name="register-user"),
    path("login/", UserLoginAPIView.as_view(), name="login-user"),
    path("profile/", UserProfileAPIView.as_view(), name="user-profile"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
]