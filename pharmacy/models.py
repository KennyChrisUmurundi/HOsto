from django.db import models
from django.utils import timezone
# Create your models here.


class Drugs(models.Model):
    name               =   models.CharField(max_length=200)
    category           =   models.CharField(max_length=300)
    pricePerUnit       =   models.CharField(max_length=300)
    quantity           =   models.CharField(max_length=300)
    purchasedPrice       =   models.CharField(max_length=300)
    supplier               = models.CharField(max_length=300)
    effects                 =   models.CharField(max_length=300)
    expire_date             = models.DateTimeField()
    created_date =   models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.name} Drugs'

    def expirationDate(self):
        return self.expire_date.strftime('%B %d %Y')


class TakenDrugs(models.Model):
    patient     =   models.CharField(max_length=200)
    drugName    =   models.CharField(max_length=200)
    quantity    =   models.IntegerField()
    totalPrice  =   models.IntegerField()
    created_date =   models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.patient} TakenDrugs'

class Category(models.Model):

    category    =   models.CharField(max_length=300)
    description =   models.CharField(max_length=300)

    def __str__(self):
        return f'{self.category}'

class DrugsSupplier(models.Model):

    name    =   models.CharField(max_length=300)
    address =   models.CharField(max_length=300)
    phone =   models.CharField(max_length=300)
    email =   models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name}'
