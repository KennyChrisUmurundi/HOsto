from django.apps import AppConfig


class ReceptionConfig(AppConfig):
    name = 'reception'

    def ready(self):
    	import reception.signals
