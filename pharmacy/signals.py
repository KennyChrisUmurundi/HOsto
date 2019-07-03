from doctor.models import InstructionsForPharmacy
from reception.models import CashPharmacyStatus
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=InstructionsForPharmacy)
def create_pharmacy(sender, instance, created, **kwargs):
	if created:
		CashPharmacyStatus.objects.create(InstructionsForPharmacy=instance)

@receiver(post_save, sender=InstructionsForPharmacy)
def save_pharmacy(sender, instance, **kwargs):
	instance.cashpharmacystatus.save()
