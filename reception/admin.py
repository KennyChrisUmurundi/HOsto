from django.contrib import admin

# Register your models here.
from .models import Patient, Appointment, Lab, Test, CashAppointmentStatus, CashLabStatus

admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Test)
admin.site.register(Lab)
admin.site.register(CashAppointmentStatus)
admin.site.register(CashLabStatus)
