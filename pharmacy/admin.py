from django.contrib import admin
from .models import Drugs,TakenDrugs,Category,DrugsSupplier

# Register your models here.
admin.site.register(Drugs)
admin.site.register(TakenDrugs)
admin.site.register(Category)
admin.site.register(DrugsSupplier)
