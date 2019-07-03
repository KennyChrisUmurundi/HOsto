from django.contrib import admin
from .models import Drugs,TakenDrugs

# Register your models here.
admin.site.register(Drugs)
admin.site.register(TakenDrugs)
