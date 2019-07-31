from django.db import models

# Create your models here.


class corpses(models.Model):

    patient=models.CharField(max_length=300)
    patient_code=models.CharField(max_length=300)
    date_of_death=models.CharField(max_length=300)
    death_report=models.CharField(max_length=500)


class Mpayment(models.Model):

    patient=models.CharField(max_length=300)
    status=models.CharField(default="Not Paid",max_length=300)
