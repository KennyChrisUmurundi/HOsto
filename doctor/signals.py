# from .models import Appointment, Lab, CashAppointmentStatus, CashLabStatus,Patient,Allotment,Room
# from doctor.models import Reports
# from Laboratory.models import Results,TestStatus
# from ward.models import PatientStatus
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
#
# @receiver(post_save, sender=Room)
# def create_appointment(sender, instance, created, **kwargs):
# 	if created:
# 		Allotment.objects.create(number=instance)
#
# @receiver(post_save, sender=Room)
# def save_appointment(sender, instance, **kwargs):
# 	instance.allotment.save()
