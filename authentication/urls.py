from django.urls import path
from .views import RegisterView, LoginView, LogoutView, AdminLoginView, StaffLoginView, PromoteToStaffView, PromoteToAdminView, RemoveFromStaffView, RemoveFromAdminView, StudentDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/login/', AdminLoginView.as_view(), name='admin-login'),
    path('staff/login/', StaffLoginView.as_view(), name='staff-login'),
    path('admin/promote-to-staff/<uuid:user_id>/', PromoteToStaffView.as_view(), name='promote-to-staff'),
    path('admin/remove-from-staff/<uuid:user_id>/', RemoveFromStaffView.as_view(), name='remove-from-staff'),
    path('admin/promote-to-admin/<uuid:user_id>/', PromoteToAdminView.as_view(), name='promote-to-admin'),
    path('admin/remove-from-admin/<uuid:user_id>/', RemoveFromAdminView.as_view(), name='remove-from-admin'),
    path('student-detail/<uuid:user_id>/', StudentDetailView.as_view(), name='student-detail'),
]