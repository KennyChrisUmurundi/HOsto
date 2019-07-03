from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as doctor_views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'doctor'
urlpatterns = [
	#path('', doctor_views.doctor_home, name='doctor-home'),
	path('patient/<slug:code>', doctor_views.patient, name='patient'),
	# path('patients/', doctor_views.AddReportView.as_view(), name='repot'),
	path('add_doctor/',doctor_views.AddDoctorView.as_view(),name='add_doctor'),
	path('scan/', doctor_views.ScanCode, name='ScanCode'),
	path('profile/', doctor_views.profile, name='doctor-profile'),
	path('patient_lab_test/<slug:code>', doctor_views.patient_lab_test, name='patient-lab'),
	path('patient_pharmacy/<slug:code>', doctor_views.send_for_pharmacy, name='patient-pharmacy'),
	path('patient_icu/<slug:code>', doctor_views.send_for_icu, name='patient-icu'),
	path('reports/<slug:code>/<int:id>', doctor_views.reports, name='reports'),
	path('C_reports/<slug:code>/<int:id>', doctor_views.C_reports, name='theReport'),
	path('C_results/<slug:code>/<int:id>', doctor_views.C_results, name='theResult'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
