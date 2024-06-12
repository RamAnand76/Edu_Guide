from rest_framework import serializers
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'phone_number')