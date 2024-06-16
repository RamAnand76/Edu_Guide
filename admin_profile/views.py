from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from authentication.permissions import IsAdmin
from authentication.models import StudentsList
from .serializers import StudentsListSerializer

class StudentsListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = StudentsList.objects.filter(user__is_staff=False, user__is_admin=False)
    serializer_class = StudentsListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        formatted_response = {student['username']: student for student in serializer.data}
        return Response(formatted_response)
