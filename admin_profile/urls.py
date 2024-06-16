from django.urls import path
from .views import StudentsListView

urlpatterns = [
    path('students/', StudentsListView.as_view(), name='students-list'),
]