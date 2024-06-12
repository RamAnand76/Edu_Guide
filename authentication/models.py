import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=15, unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff_member = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class StudentsList(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    # Add any other fields if necessary
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    

class BlacklistedAccessToken(models.Model):
    token = models.CharField(max_length=500, unique=True)
    blacklisted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token