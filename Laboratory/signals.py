from .models import Appointment, Lab, CashAppointmentStatus, CashLabStatus
from doctor.models import Reports
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Appointment)
def create_appointment_report(sender, instance, created, **kwargs):
	if created:
		Reports.objects.create(appointment=instance)

@receiver(post_save, sender=Appointment)
def save_appointment_report(sender, instance, **kwargs):
	instance.reports.save()
