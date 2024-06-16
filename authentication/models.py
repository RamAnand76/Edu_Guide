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
    
    # Adding new fields for storing student-specific information
    dob = models.DateField()
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    graduation_year = models.IntegerField()

    #gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    #major = models.CharField(max_length=100, null=True, blank=True)

    intended_degree = models.CharField(max_length=50)
    intended_field_of_study = models.CharField(max_length=100)
    preferred_location = models.CharField(max_length=100)
    
    APPLICATION_STATUS_CHOICES = [
        ('Interested', 'Interested'),
        ('Not Interested', 'Not Interested'),
        ('Callback', 'Callback'),
        ('No Response', 'No Response'),
    ]
    application_status = models.CharField(max_length=15, choices=APPLICATION_STATUS_CHOICES)

    # Add any other fields if necessary
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    

class BlacklistedAccessToken(models.Model):
    token = models.CharField(max_length=500, unique=True)
    blacklisted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token
