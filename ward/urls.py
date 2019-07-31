from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as ward_views

app_name = 'ward'
urlpatterns = [
	path('', ward_views.ward_home, name='ward-home'),
	path('patient/<slug:code>', ward_views.inpatient_info, name='inpatient_info'),
	path('patientStatus/<slug:code>/<int:id>', ward_views.patient_status_update, name='patient-status'),
	path('nurse/home', ward_views.nurse_home, name='nurse-home'),
	path('finalReport/create/<slug:code>/<int:id>', ward_views.patientFinalReport, name='patient-finalReport'),
    #path('create/', ward_views.PatientFinalReportCreateView.as_view(), name='create_finalReport'),
	#path('nurse/PatientTreatment/<slug:code>/<int:id>', ward_views.patient_treatment, name='patient-treatment'),
	
]