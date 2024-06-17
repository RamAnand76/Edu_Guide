from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from admin_profile.models import StudentStaffAssignment
from authentication.permissions import IsAdmin
from authentication.models import CustomUser, StudentsList
from .serializers import StudentStaffAssignmentSerializer, StudentsListSerializer
from rest_framework import status


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
    
class AssignStudentToStaffView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = StudentStaffAssignment.objects.all()
    serializer_class = StudentStaffAssignmentSerializer

    def create(self, request, *args, **kwargs):
        student_id = request.data.get('student')
        staff_id = request.data.get('staff')

        # Perform any necessary validation here
        if not student_id or not staff_id:
            return Response({"detail": "Both student and staff must be provided."}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure student is not staff or admin
        try:
            student = CustomUser.objects.get(id=student_id)
            if student.is_staff or student.is_admin:
                return Response({"detail": "Cannot assign a staff or admin as a student."}, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({"detail": "Student not found."}, status=status.HTTP_404_NOT_FOUND)

        # Ensure staff is actually a staff member
        try:
            staff = CustomUser.objects.get(id=staff_id)
            if not staff.is_staff:
                return Response({"detail": "Assigned staff member must be a staff user."}, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({"detail": "Staff not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if student is already assigned to a staff member
        if StudentStaffAssignment.objects.filter(student=student).exists():
            return Response({"detail": "This student is already assigned to a staff member."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the assignment
        assignment = StudentStaffAssignment(student=student, staff=staff)
        assignment.save()

        serializer = self.get_serializer(assignment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
