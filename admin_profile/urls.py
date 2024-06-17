from django.urls import path
from .views import AssignStudentToStaffView, StudentsListView

urlpatterns = [
    path('students/', StudentsListView.as_view(), name='students-list'),
    path('assign-student-to-staff/', AssignStudentToStaffView.as_view(), name='assign-student-to-staff'),
]