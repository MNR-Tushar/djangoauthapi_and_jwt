
from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("users", CustomUserView, basename="users")

urlpatterns = [
    path("register/", UserRegisterAPIView.as_view(), name="register-user"),
    path("login/", UserLoginAPIView.as_view(), name="login-user"),
    path("profile/", UserProfileAPIView.as_view(), name="user-profile"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("change-password/", UserChangePasswordAPIView.as_view(), name="change-password"),
    path("send-reset-password-email/", SendPasswordResetEmailAPIView.as_view(), name="send-reset-password-email"),
    path("reset-password/<uid>/<token>/", UserPasswordResetAPIView.as_view(), name="reset-password"),
    path("send-verification-email/", SendEmailVerificationAPIView.as_view(), name="send-verification-email"),
    path("verify-email/<uid>/<token>/", VerifyEmailAPIView.as_view(), name="verify-email"),
    path("", include(router.urls)),
]