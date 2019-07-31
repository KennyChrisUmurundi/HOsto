from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from reception.models import Patient, Appointment
from django.db.models import Sum
from django.contrib.auth.decorators import login_required

from .models import PatientStatus, PatientReport

from . import forms as ward_forms

import hashlib
 
# Create your views here.
@login_required(login_url='/')
def ward_home(request):
	PatientCode 		= 	request.POST.get('PatientCode', False)

	context = {
		'PatientByCode' 			:	Patient.objects.filter(code__icontains=PatientCode),
	}

	return render(request, 'ward/ward_home.html', context)

@login_required(login_url='/')
def inpatient_info(request, code):
	thecode = code

	apptmt = Appointment.objects.filter(patient=thecode).aggregate(Sum('price'))['price__sum']

	context = {
		'CurrentPatient'	:	Patient.objects.filter(code=thecode),
		'reception' 		:	Appointment.objects.filter(patient=thecode),
		'RecTotalPrice'		:	apptmt,	
	}

	return render(request, 'ward/inpatient_info.html', context)

@login_required(login_url='/')
def patient_status_update(request, code, id):

	return render(request, 'ward/patientStatus.html')

@login_required(login_url='/')
def patient_status_update(request, code, id):

	app_instance 	=	get_object_or_404(Patient, code=code, id=id)
	update_patientStatus_form 	= 	ward_forms.PatientStatusUpdate(request.POST or None, instance=app_instance.patientstatus)
	
	if request.method == 'POST':

		update_patientStatus_form 	= 	ward_forms.PatientStatusUpdate(request.POST or None, instance=app_instance.patientstatus)
		
		if update_patientStatus_form.is_valid():
			u_patientStatus 				= 	update_patientStatus_form.save(commit=False)
			u_patientStatus.status			=	app_instance.patientstatus.status
			update_patientStatus_form.save()
			print('success')
			if request.user.role.role == 'is_doctor':
				return redirect('doctor:patient', code=app_instance.code)
			elif request.user.role.role == 'is_nurse':
				return redirect('ward:nurse-home')			

		else:
			print('not valid') 

	else:
		
		update_patientStatus_form 	= 	ward_forms.PatientStatusUpdate(instance=app_instance.patientstatus)

	context = {
		'update_patientStatus_form' 		: 	update_patientStatus_form,
		'patient' 							: 	Patient.objects.filter(code=code, id=id),
	}

	return render(request, 'ward/patientStatus.html', context)

def nurse_home(request):

	context = {
		'inpatient'		:	PatientStatus.objects.filter(status='InPatient')
	}

	return render(request, 'ward/nurse_home.html', context)

def patientFinalReport(request, code, id):

	if request.method == 'POST':
		patient = Patient.objects.get(id=request.POST['patient'])
		prescription = request.POST['prescription']
		n = len(prescription.split()) 
		print(type(n))
		print(n)
		report = request.POST['report']
		p_report = PatientReport.objects.filter(patient=patient)
		if not p_report:
			print('Yes')
			PatientReport.objects.create(
		 		patient 				=	patient,	
		 		doctor_prescription 	= 	prescription,
		 		nurse_report 			=	report
		 	)
		else:
			for patient_report in p_report:
				p = len(patient_report.doctor_prescription.split())
				print(type(p))
				print(p) 
				if p is not None and n == p:
					print('Nothing was modify')
				else:
					print('Yes')
					# PatientReport.objects.create(
		 		# 		patient 				=	patient,	
		 		# 		doctor_prescription 	= 	prescription,
		 		# 		nurse_report 			=	report
		 		# 	)

	return HttpResponse('')



