from django.db import models
from authentication.models import CustomUser  # Assuming CustomUser is in the authentication app

class StudentStaffAssignment(models.Model):
    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='assigned_student')
    staff = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='assigned_staff')
    assigned_date = models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together = ('student', 'staff')

    def __str__(self):
        return f"{self.student.username} assigned to {self.staff.username}"
