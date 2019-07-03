from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as reception_views

app_name = 'reception'
urlpatterns = [
	path('', reception_views.reception_home, name='reception-home'),
	path('add_patient/', reception_views.AddPatientView.as_view(), name='add-patient'),
	#path('add_appointment/<slug:code>', reception_views.AddAppointmentView.as_view(), name='add-appointment'),
	path('add_appointment/<slug:code>', reception_views.add_appointment, name='add-appointment'),
	path('barcode/<slug:code>', reception_views.gen_barcode, name='gen_barcode'),
	path('patient_info/<slug:code>', reception_views.patient_info, name='patient-info'),
	path('payment_appointment_update/<slug:code>/<int:id>', reception_views.payment_appointment_update, name='payment-appointment-update'),
	path('payment_lab_update/<slug:code>/<int:id>', reception_views.payment_lab_update, name='payment-lab-update'),
# 	path('payment_pharmacy_update/<slug:code>/<int:id>', reception_views.payment_pharmacy_update, name='payment-pharmacy-update'),
 ]
