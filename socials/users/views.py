from rest_framework import generics
from .models import CustomUser
from .serializers import UserRegistrationSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.object.all()
    serializer_class = UserRegistrationSerializer