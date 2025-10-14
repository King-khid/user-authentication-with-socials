from rest_framework import serializers
from .models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'phone', 'password']

        def create(self, validated_data):
            user = CustomUser.Objects.Create_user(**validated_data)
            return user
