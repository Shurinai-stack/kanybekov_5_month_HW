from django.urls import path
from .views import (
    RegistrationAPIView,
    ConfirmUserAPIView,
    AuthAPIView,
)

urlpatterns = [
    path('register/', RegistrationAPIView.as_view()),
    path('confirm/', ConfirmUserAPIView.as_view()),
    path('login/', AuthAPIView.as_view()),
]
