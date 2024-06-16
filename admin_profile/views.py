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
        
        # Constructing the desired response structure
        formatted_response = {}
        for student_data in serializer.data:
            username = student_data['user']['username']
            formatted_response[username] = {
                **student_data['user'],  # Include all fields from the user
                'dob': student_data['dob'],
                'gender': student_data['gender'],
                'city': student_data['city'],
                'state': student_data['state'],
                'pin_code': student_data['pin_code'],
                'graduation_year': student_data['graduation_year'],
                'intended_degree': student_data['intended_degree'],
                'intended_field_of_study': student_data['intended_field_of_study'],
                'preferred_location': student_data['preferred_location'],
                'application_status': student_data['application_status'],
                'comments': student_data['comments'],
                'enrollment_date': student_data['enrollment_date']
            }
        
        return Response(formatted_response)