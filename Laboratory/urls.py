from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as lab_views

app_name = 'Laboratory'
urlpatterns = [

	path('scan/', lab_views.lab_scanBarcode, name='scanBarcode'),
    path('lab_patient/<slug:code>',lab_views.lab_patient,name='lab_patient'),
	path('performTest/<slug:code>/<int:id>', lab_views.perform_test, name='Test'),
	# path('CheckResults/<slug:code>/', lab_views.results, name='results'),


    ]
