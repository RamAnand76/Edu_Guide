from rest_framework import serializers
from authentication.models import StudentsList, CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']

class StudentsListSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = StudentsList
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active',
            'dob', 'gender', 'city', 'state', 'pin_code',
            'graduation_year', 'intended_degree', 'intended_field_of_study',
            'preferred_location', 'application_status', 'comments', 'enrollment_date'
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        return {
            rep['username']: {
                'id': rep['id'],
                'username': rep['username'],
                'email': rep['email'],
                'first_name': rep['first_name'],
                'last_name': rep['last_name'],
                'is_staff': rep['is_staff'],
                'is_active': rep['is_active'],
                'dob': rep['dob'],
                'gender': rep['gender'],
                'city': rep['city'],
                'state': rep['state'],
                'pin_code': rep['pin_code'],
                'graduation_year': rep['graduation_year'],
                'intended_degree': rep['intended_degree'],
                'intended_field_of_study': rep['intended_field_of_study'],
                'preferred_location': rep['preferred_location'],
                'application_status': rep['application_status'],
                'comments': rep['comments'],
                'enrollment_date': rep['enrollment_date']
            }
        }
