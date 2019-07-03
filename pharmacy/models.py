from django.db import models
from django.utils import timezone
# Create your models here.


class Drugs(models.Model):
    name               =   models.CharField(max_length=200)
    category           =   models.CharField(max_length=300)
    pricePerUnit       =   models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} Drugs'


class TakenDrugs(models.Model):
    patient     =   models.CharField(max_length=200)
    drugName    =   models.CharField(max_length=200)
    status      =   models.CharField(default='Not Paid', max_length=10)
    quantity    =   models.IntegerField()
    totalPrice  =   models.IntegerField()
    created_date =   models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.patient} TakenDrugs'
