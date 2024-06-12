from django.contrib import admin
from .models import BlacklistedAccessToken, CustomUser, StudentsList

admin.site.register(BlacklistedAccessToken)
admin.site.register(CustomUser)
admin.site.register(StudentsList)