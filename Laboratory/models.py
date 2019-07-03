from django.db import models
from reception.models import Lab

# Create your models here.


class Results(models.Model):
    patient     =   models.CharField(max_length=200)
    findings    =   models.CharField(max_length=300)
    tests       =   models.OneToOneField(Lab,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tests.patient} Results'

class TestStatus(models.Model):
	test 					=	models.OneToOneField(Lab, on_delete=models.CASCADE)
	patient 				= 	models.CharField(max_length=300)
	status 					=	models.CharField(default='Not Done', max_length=10)

	def __str__(self):
		return f'{self.test.patient} TestStatus'
