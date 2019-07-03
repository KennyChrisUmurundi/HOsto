from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Role, UserPersonalData

@receiver(post_save, sender=User)
def create_userpersonaldata(sender, instance, created, **kwargs):
	if created:
		UserPersonalData.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_userpersonaldata(sender, instance, **kwargs):
	instance.userpersonaldata.save()

@receiver(post_save, sender=User)
def create_user_role(sender, instance, created, **kwargs):
	if created:
		Role.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_role(sender, instance, **kwargs):
	instance.role.save()