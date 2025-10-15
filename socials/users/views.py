from rest_framework import generics
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import status
from .serializers import LoginSerializer
from .serializers import UserRegistrationSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer

class LoginView(APIView):
    def post (self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access':str(refresh.access_token),
            'email': user.email,
            'first_name': user.first_name,
        }, status=status.HTTP_200_OK)