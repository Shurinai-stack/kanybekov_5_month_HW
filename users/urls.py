from django.urls import path
from .views import (
    RegistrationAPIView,
    ConfirmUserAPIView,
    CustomTokenObtainPairView,
)
from .views import GoogleOAuthAPIView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view()),
    path('confirm/', ConfirmUserAPIView.as_view()),
    path('login/', CustomTokenObtainPairView.as_view()),
    path('google/', GoogleOAuthAPIView.as_view()),
]
