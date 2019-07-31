from django.contrib import admin

from .models import PatientStatus, PatientReport

# Register your models here.

admin.site.register(PatientStatus),
admin.site.register(PatientReport),