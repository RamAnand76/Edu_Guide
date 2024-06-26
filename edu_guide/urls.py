from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('user/', include('user_profile.urls')),
    path("admin-profile/", include("admin_profile.urls"),)
]
