from rest_framework import serializers
from authentication.models import CustomUser, StudentsList

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']

class StudentsListSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = StudentsList
        fields = [
            'user', 'dob', 'gender', 'city', 'state', 'pin_code', 'graduation_year',
            'intended_degree', 'intended_field_of_study', 'preferred_location', 
            'application_status', 'comments', 'enrollment_date'
        ]