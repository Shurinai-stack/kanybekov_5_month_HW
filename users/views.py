import random
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .serializers import UserAuthSerializer,UserConfirmSerializer,UserRegisterSerializer
from .models import ConfirmCode

class AuthAPIView(APIView):
    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            token = Token.objects.get_or_create(user=user)
            return Response({'key': token.key})
        
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class RegistrationAPIView(APIView):
    def post(self,request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = User.objects.create_user(
            username=username,
            password=password,
            is_active=False
        )

        code = ''.join([str(random.randint(0,9)) for _ in range(6)])

        ConfirmCode.objects.create(
            user=user,
            code=code
        )

        return Response(data={'user_id': user.id},
                        status=status.HTTP_201_CREATED)

class ConfirmUserAPIView(APIView):
    def post(self, request):
        serializer = UserConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        code = serializer.validated_data.get('code')

        try:
            confirm = ConfirmCode.objects.get(code=code)
        except ConfirmCode.DoesNotExist:
            return Response(
                {'error': 'invalid confirm code'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user = confirm.user
        user.is_active = True
        user.save()

        confirm.delete()

        return Response(
            {'message': 'User confirm OK'},
            status=status.HTTP_200_OK
        )