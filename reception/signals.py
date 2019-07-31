from .models import Appointment, Lab, CashAppointmentStatus, CashLabStatus,Patient
from doctor.models import Reports
from Laboratory.models import Results,TestStatus
from ward.models import PatientStatus
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Appointment)
def create_appointment(sender, instance, created, **kwargs):
	if created:
		CashAppointmentStatus.objects.create(appointment=instance)

@receiver(post_save, sender=Appointment)
def save_appointment(sender, instance, **kwargs):
	instance.cashappointmentstatus.save()

@receiver(post_save, sender=Lab)
def create_lab_test(sender, instance, created, **kwargs):
	if created:
		CashLabStatus.objects.create(labTest=instance)

@receiver(post_save, sender=Lab)
def save_lab_test(sender, instance, **kwargs):
	instance.cashlabstatus.save()

@receiver(post_save, sender=Lab)
def create_test_status(sender, instance, created, **kwargs):
	if created:
		TestStatus.objects.create(test=instance)

@receiver(post_save, sender=Lab)
def save_test_status(sender, instance, **kwargs):
	instance.teststatus.save()

@receiver(post_save, sender=Appointment)
def create_appointment_report(sender, instance, created, **kwargs):
	if created:
		Reports.objects.create(appointment=instance)

@receiver(post_save, sender=Appointment)
def save_appointment_report(sender, instance, **kwargs):
	instance.reports.save()

@receiver(post_save, sender=Lab)
def create_lab_results(sender, instance, created, **kwargs):
	if created:
		Results.objects.create(tests=instance)

@receiver(post_save, sender=Lab)
def save_lab_results(sender, instance, **kwargs):
	instance.results.save()

@receiver(post_save, sender=Patient)
def create_patient_status(sender, instance, created, **kwargs):
	if created:
		PatientStatus.objects.create(patient=instance)

@receiver(post_save, sender=Patient)
def save_patient_status(sender, instance, **kwargs):
	instance.patientstatus.save()
