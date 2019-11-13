from django.contrib import admin

# Register your models here.
from .models import Doctor,Reports,Category,InstructionsForPharmacy,InstructionsForNurse,Prices,Room,Allotment

admin.site.register(Category)
admin.site.register(Doctor)
admin.site.register(Reports)
admin.site.register(Prices)
admin.site.register(InstructionsForPharmacy)
admin.site.register(InstructionsForNurse)
admin.site.register(Room)
admin.site.register(Allotment)
