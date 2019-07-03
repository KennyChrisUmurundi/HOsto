from django.contrib import admin

# Register your models here.
from .models import Doctor,Reports,Category,InstructionsForPharmacy

admin.site.register(Category)
admin.site.register(Doctor)
admin.site.register(Reports)
admin.site.register(InstructionsForPharmacy)
