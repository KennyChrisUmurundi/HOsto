from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from reception.models import Appointment

# Create your models here.


class Category(models.Model):
	name 					=	models.CharField(max_length=30)
	created_date			=	models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

class Doctor(models.Model):
	category 				=	models.ForeignKey(Category, on_delete=models.CASCADE)
	name 					=	models.CharField(max_length=300)
	created_date			=	models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name

class Prices(models.Model):
	doctor 					=	models.ForeignKey(Doctor, on_delete=models.CASCADE)
	amount 					=	models.IntegerField(default=0)


class Reports(models.Model):

    appointment 	=	    models.OneToOneField(Appointment, on_delete=models.CASCADE)
    patient         =       models.CharField(max_length=200)
    report          =       models.TextField()
    created_date    =   	models.DateTimeField(default=timezone.now)

    class Meta:
         get_latest_by = 'created_date'

    def __str__(self):
        return f'{self.appointment.patient} Reports'


class InstructionsForPharmacy(models.Model):


    patient         =       models.CharField(max_length=200)
    instructions    =       models.TextField()
    created_date    =   	models.DateTimeField(default=timezone.now)

    class Meta:
         get_latest_by = 'created_date'

    def __str__(self):
        return f'{self.patient} InstructionsForPharmacy'

class InstructionsForNurse(models.Model):


    patient         =       models.CharField(max_length=200)
    instructions    =       models.TextField()
    created_date    =   	models.DateTimeField(default=timezone.now)

    class Meta:
         get_latest_by = 'created_date'

    def __str__(self):
        return f'{self.patient} InstructionsForNurse'
