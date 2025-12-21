from django.urls import path
from .views import (
    registration_api_view,
    confirm_user_api_view,
    AuthAPIView
)

urlpatterns = [
    path('register/', registration_api_view),
    path('confirm/', confirm_user_api_view),
    path('login/', AuthAPIView.as_view()),
]
