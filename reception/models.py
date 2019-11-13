
from random import randrange


from django.contrib import admin
from django.db import models
from django.db import models
from django.utils import timezone
# from doctor.models import InstructionsForPharmacy


# Create your models here.

CHARSET = '0123456789ABCDEFGHJKMNPQRSTVWXYZ'
LENGTH = 5
MAX_TRIES = 32

class Patient(models.Model):
	firstname 				= 	models.CharField(max_length=200)
	lastname 				= 	models.CharField(max_length=200)
	gender 	 				=	models.CharField(max_length=300)
	phone 					=	models.CharField(max_length=300)
	dob 					=	models.CharField(max_length=300)
	age 					= 	models.IntegerField()
	status					=	models.CharField(max_length=20)
	address					=	models.TextField()
	email					=	models.EmailField(null=True,blank=True)
	occupation				=	models.CharField(max_length=300)
	payment					=	models.CharField(max_length=300)
	code 					=	models.CharField(max_length=200, editable=False, unique=True)
	image 					= 	models.FileField(upload_to='profile_pics',null=True,blank=True)
	test_data 				= 	models.CharField("Test Data", max_length=128) # TODO: test_data
	created_date			=	models.DateTimeField(default=timezone.now)
	patient_identification		=	models.CharField(max_length=300)
	blood_group					=	models.CharField(max_length=100)
	allergies					=	models.CharField(max_length=500)
	diabetic					= 	models.CharField(max_length=100)
	weight						=	models.CharField(max_length=100)
	high_blood_pressure					=	models.CharField(max_length=100)
	seizures					=	models.CharField(max_length=500)
	liver_desease					= 	models.CharField(max_length=100)
	ulcers						=	models.CharField(max_length=100)
	gout					=	models.CharField(max_length=100)
	heart_desease					=	models.CharField(max_length=500)
	heart_valve_desease					= 	models.CharField(max_length=100)
	lung_desease						=	models.CharField(max_length=100)
	cancer					=	models.CharField(max_length=100)
	hiv					=	models.CharField(max_length=500)
	thyroid_desease					= 	models.CharField(max_length=100)




	class Meta:
		verbose_name 		= "Patient"
		verbose_name_plural = "Patients"

	def __unicode__(self):
		return "%s: %s" % (self.code, self.firstname)

	def save(self, *args, **kwargs):
		loop_num = 0
		unique = False
		while not unique:
			if loop_num < MAX_TRIES:
				new_code = self.lastname[0:2]+''+self.firstname[0:2]
				for i in range(LENGTH):
					new_code += CHARSET[randrange(0, len(CHARSET))]
				if not Patient.objects.filter(code=new_code) and not self.code:
					self.code = new_code
					unique = True
				elif self.code is not None:
					self.code = self.code
					unique = True
				loop_num += 1
			else:
				raise ValueError("Couldn't generate a unique code.")
			super(Patient, self).save(*args, **kwargs)

class Appointment(models.Model):
	patient 				= 	models.CharField(max_length=300)
	price 					=	models.IntegerField(default=0)
	doctor 	 				= 	models.CharField(max_length=200)
	department 				=	models.CharField(max_length=200)
	created_date			=	models.DateTimeField(default=timezone.now)
	# expired_on 				=	models.DateTimeField(default=add_min())
	class Meta:
         get_latest_by = 'created_date'

	def __str__(self):
		return 'Appointment with {}'.format(self.doctor)


class Test(models.Model):
	name 					=	models.CharField(max_length=300)
	price 					=	models.IntegerField()
	created_date			=	models.DateTimeField(default=timezone.now)

class Lab(models.Model):
	patient 				= 	models.CharField(max_length=300)
	tests 	 				= 	models.TextField()
	status 					=	models.CharField(default='Not done', max_length=10)
	totalPrice 				=	models.IntegerField()
	created_date			=	models.DateTimeField(default=timezone.now)


class CashAppointmentStatus(models.Model):
	appointment 			=	models.OneToOneField(Appointment, on_delete=models.CASCADE)
	patient 				= 	models.CharField(max_length=300)
	status 					=	models.CharField(default='Unpaid', max_length=10)
	payment_type			=	models.CharField(max_length=50)
	created_date			=	models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.appointment.patient} CashAppointmentStatus'

class CashLabStatus(models.Model):
	labTest 				=	models.OneToOneField(Lab, on_delete=models.CASCADE)
	patient 				= 	models.CharField(max_length=300)
	status 					=	models.CharField(default='Unpaid', max_length=10)
	payment_type			=	models.CharField(max_length=50)
	created_date			=	models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.labTest.patient} CashLabStatus'

# class CashPharmacyStatus(models.Model):
# 	prescription 			=	models.OneToOneField(InstructionsForPharmacy, on_delete=models.CASCADE)
# 	patient 				= 	models.CharField(max_length=300)
# 	status 					=	models.CharField(default='Unpaid', max_length=10)
#
# 	def __str__(self):
# 		return f'{self.InstructionsForPharmacy.patient} InstructionsForPharmacy'
