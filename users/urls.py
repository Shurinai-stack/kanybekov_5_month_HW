from django.urls import path
from .views import (
    RegistrationAPIView,
    ConfirmUserAPIView,
    CustomTokenObtainPairView,
)

urlpatterns = [
    path('register/', RegistrationAPIView.as_view()),
    path('confirm/', ConfirmUserAPIView.as_view()),
    path('login/', CustomTokenObtainPairView.as_view()),
]
