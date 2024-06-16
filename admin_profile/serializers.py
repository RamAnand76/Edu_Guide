from rest_framework import serializers
from authentication.models import StudentsList, CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']

class StudentsListSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()  # Assuming you have a serializer for CustomUser

    class Meta:
        model = StudentsList
        fields = '__all__'  # Include all fields of the StudentsList model

    def create(self, validated_data):
        # Custom create method if needed
        return StudentsList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Custom update method if needed
        instance.dob = validated_data.get('dob', instance.dob)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.pin_code = validated_data.get('pin_code', instance.pin_code)
        instance.graduation_year = validated_data.get('graduation_year', instance.graduation_year)
        instance.intended_degree = validated_data.get('intended_degree', instance.intended_degree)
        instance.intended_field_of_study = validated_data.get('intended_field_of_study', instance.intended_field_of_study)
        instance.preferred_location = validated_data.get('preferred_location', instance.preferred_location)
        instance.application_status = validated_data.get('application_status', instance.application_status)
        instance.comments = validated_data.get('comments', instance.comments)  # New field
        instance.save()
        return instance