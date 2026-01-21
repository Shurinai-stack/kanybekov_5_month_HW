import random

from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import (
    UserConfirmSerializer,
    UserRegisterSerializer,
    CustomTokenObtainPairSerializer
)
from .models import ConfirmCode

User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        user = User.objects.create_user(
            email=email,
            password=password,
            is_active=False
        )

        code = ''.join(str(random.randint(0, 9)) for _ in range(6))

        ConfirmCode.objects.create(
            user=user,
            code=code
        )

        return Response(
            {"user_id": user.id},
            status=status.HTTP_201_CREATED
        )

class ConfirmUserAPIView(APIView):
    def post(self, request):
        serializer = UserConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        code = serializer.validated_data.get('code')

        try:
            confirm = ConfirmCode.objects.get(code=code)
        except ConfirmCode.DoesNotExist:
            return Response(
                {"error": "invalid confirm code"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = confirm.user
        user.is_active = True
        user.save()

        confirm.delete()

        return Response(
            {"message": "User confirm OK"},
            status=status.HTTP_200_OK
        )