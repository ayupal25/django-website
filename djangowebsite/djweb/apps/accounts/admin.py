from django.contrib import admin
from .models import UserPersona, UserProfile
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(UserPersona)