from django.shortcuts import render,redirect
from reception.models import Patient,Appointment,Lab
from reception.forms import AddPatientForm
from django.views.generic import CreateView, DetailView, UpdateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

# Create your views here.


def er_home(request):

	if request.method == 'POST':
		name 		= 	request.POST.get('name', False)
		add_patient	= AddPatientForm(request.POST or None)

		if add_patient.is_valid():
			patient=add_patient.save()
			return redirect('reception:add-appointment', code=patient.code)

		add_patient	= AddPatientForm()
		context = {
			'PatientByFirstname'			:	Patient.objects.filter(Q(firstname__icontains=name)|
			 															Q(lastname__icontains=name)),
			'form'	:	add_patient
		}

		return render(request,'search_for_patient.html', context)

	return render(request,'search_for_patient.html')

def patient_info(request, code):

	theCode = code

	context = {
		'patientInfo'				:	Patient.objects.filter(code=theCode),
		'tests'					:	Lab.objects.filter(patient=theCode),
		'history_appointment'	:	Appointment.objects.filter(patient=theCode),
		'history_lab'			:	Lab.objects.filter(patient=theCode),
		#'reports'			:	Reports.objects.filter(patient=code),

	}
	return render(request, 'appointment.html', context)
