from django.urls import path
from .views import UserDetailView

urlpatterns = [
    path('details/', UserDetailView.as_view(), name='user-details'),
]