from django.db import models
from doctor.models import InstructionsForNurse
# Create your models here.

class icuFindings(models.Model):

    Instructions=   models.OneToOneField(InstructionsForNurse, on_delete=models.CASCADE)
    patient     =   models.CharField(max_length=200)
    findings    =   models.CharField(max_length=200)
    Status      =   models.CharField(default='Not Done', max_length=10)
