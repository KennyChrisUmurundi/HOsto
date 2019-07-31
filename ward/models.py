from django.db import models
from reception.models import Patient
from django.utils import timezone

# Create your models here.

class PatientStatus(models.Model):
	patient 			=	models.OneToOneField(Patient, on_delete=models.CASCADE)
	status 				=	models.CharField(default='OutPatient', max_length=10)
	prescription 		=	models.TextField()
	report 		 		=	models.TextField()

	def __str__(self):
		return f'{self.patient.code} Status'

class PatientReport(models.Model):
	patient 			=	models.ForeignKey(Patient, on_delete=models.CASCADE)
	doctor_prescription = 	models.TextField()
	nurse_report 		=	models.TextField()
	created_date 		=	models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.patient.code}' + ' '+ f'{self.created_date} WardFinalReport'

