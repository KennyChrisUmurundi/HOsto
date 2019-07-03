from django.contrib import admin
from .models import UserPersonalData, Role

# Register your models here.
admin.site.register(UserPersonalData)
admin.site.register(Role)