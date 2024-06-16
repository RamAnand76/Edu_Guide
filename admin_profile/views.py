from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsAdmin
from authentication.models import StudentsList
from admin_profile.serializers import StudentsListSerializer

class StudentsListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    
    queryset = StudentsList.objects.filter(user__is_staff=False, user__is_admin=False)
    serializer_class = StudentsListSerializer