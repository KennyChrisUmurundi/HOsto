from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Role(models.Model):
	user 	= 	models.OneToOneField(User, on_delete=models.CASCADE)
	role 	=	models.CharField(default='new_user', max_length=20)
	status 	=	models.CharField(default='active', max_length=10)

	def __str__(self):
		return f'{self.user.username} Role'

class UserPersonalData(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
	role =	models.CharField(max_length=30)

	def __str__(self):
		return f'{self.user.username} UserPersonalData'