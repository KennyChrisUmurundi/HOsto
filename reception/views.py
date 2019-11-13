from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DetailView, UpdateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, timedelta

from . import forms as reception_forms
from .models import Patient, Appointment,Lab,CashAppointmentStatus,CashLabStatus
from doctor.models import Reports, Doctor, Category,Prices
from mortury.models import corpses,Mpayment
from . import mybarcode
from itertools import chain
# Create your views here.
@login_required(login_url='/')
def reception_home(request):

	if request.method == 'POST':
		name 		= 	request.POST.get('name', False)
		print(name)

		context = {
			'PatientByFirstname'			:	Patient.objects.filter(firstname__icontains=name),
		}

		return render(request, 'reception/reception_home.html', context)
	context = {
		'PatientByFirstname'			:	Patient.objects.all().order_by('-created_date'),
	}

	return render(request, 'reception/reception_home.html',context)

def add_patient(request):
	if request.method == 'POST':
		print('vyakunze')
		add_patient = reception_forms.AddPatientForm(request.POST or None)
		if add_patient.is_valid(self):
			patient 			=	add_patient.save(commit=False)
			patient.user 		= 	self.request.user
			patient.save()
			print('ik')
			messages.success(request,f'Added successfully')
			return redirect('reception:add-appointment', code=patient.code)
	add_patient=reception_forms.AddPatientForm()
	context={
            'form'     :   add_patient,
    }
	return render(request, 'reception/add_patient.html', context)

class AddPatientView(LoginRequiredMixin, CreateView):
	model = Patient
	form_class = reception_forms.AddPatientForm
	template_name = 'reception/add_patient.html'

	def form_valid(self, form):
		patient 			=	form.save(commit=False)
		patient.user 		= 	self.request.user
		patient.save()
		print(patient.code)
		messages.add_message(self.request, messages.SUCCESS, f'Patient Created')

		return redirect('reception:add-appointment', code=patient.code)

def add_patient_medical(request,id):
	object  =   get_object_or_404(Patient,id=id)
	if request.method == 'POST':
		print('vyakunze')
		add_patient = reception_forms.AddPatientMedicalForm(request.POST,instance=object)
		if add_patient.is_valid():
			add_patient.save()
			print('ik')
			messages.success(request,f'Added successfully')
			# return redirect('reception:add-appointment')
	add_patient=reception_forms.AddPatientMedicalForm(instance=object)
	context={
            'form'     :   add_patient,
			'patient':     Patient.objects.filter(id=id).order_by('-created_date'),
    }
	return render(request, 'reception/patientMedicalForm.html', context)
# class AddAppointmentView(LoginRequiredMixin, CreateView):
#  	model = Appointment, Lab
#  	form_class 	= 	reception_forms.AddAppointmentForm
#  	form2_class	=	reception_forms.AddLabForm
#  	template_name = 'reception/add_appointment.html'

#  	def form_valid(self, form):
#  		appointment 			=	form.save(commit=False)
#  		#Appointment.patient 	= 	appointment.patient
#  		print (appointment.patient)
#  		#appointment.save()
#  		messages.add_message(self.request, messages.SUCCESS, f'Appointment Created')
#  		return redirect('reception:gen_barcode', code=appointment.patient)

#  	def get_context_data(self, **kwargs):
#  		context = super(AddAppointmentView, self).get_context_data(**kwargs)
#  		context['patient'] = Patient.objects.filter(code=self.kwargs.get('code'))
#  		return context
@login_required(login_url='/')
def add_appointment(request, code):

	if request.method == 'POST':
		add_apptmt_form 	= 	reception_forms.AddAppointmentForm(request.POST or None)
		add_lab_form		=	reception_forms.AddLabForm(request.POST or None)

		if add_apptmt_form.is_valid():
			if request.POST.get('category_select') is not None:
				apptmt 				= 		add_apptmt_form.save(commit=False)
				data 				=		add_apptmt_form.cleaned_data.get
				doctor_selected 	=		Doctor.objects.filter(name=data('doctor_select'))
				apptmt.doctor 		=		request.POST.get('doctor_select')
				apptmt.patient		= 		request.POST.get('patient')
				apptmt.department		= 		request.POST.get('category_select')
				price_select 		=		Prices.objects.filter(amount=data('price_select'))
				apptmt.price 		=		request.POST.get('price_select')
				add_apptmt_form.save()

				return redirect('reception:gen_barcode', code=apptmt.patient)


			else:
				if add_lab_form.is_valid():
					lab 					=	add_lab_form.save(commit=False)
					lab.patient 			= 	request.POST.get('patient')
					lab.totalPrice 			=	request.POST.get('totalPrice')
					add_lab_form.save()
					#print('Success')
					return redirect('reception:gen_barcode', code=lab.patient)

		else:
			print('not valid')

	else:
		add_apptmt_form 	= 	reception_forms.AddAppointmentForm()
		add_lab_form		=	reception_forms.AddLabForm()


	context = {
		'add_apptmt_form' 	: 	add_apptmt_form,
		'add_lab_form'		:	add_lab_form,
		'patient' 			: 	Patient.objects.filter(code=code),

	}

	return render(request, 'reception/add_appointment.html', context)

@login_required(login_url='/')
def gen_barcode(request, code):
    #instantiate a drawing object
    #patient = Patient.objects.filter()
    p_code = code
    d = mybarcode.MyBarcodeDrawing(p_code)
    binaryStuff = d.asString('pdf')
    response = HttpResponse(binaryStuff, 'image/pdf')
    return response

def patient_info(request, code):

	theCode = code

	context = {
		'scanCode'				:	Patient.objects.filter(code=theCode),
		'tests'					:	Lab.objects.filter(patient=theCode),
		'history_appointment'	:	Appointment.objects.filter(patient=theCode).order_by('-created_date'),
		'history_lab'			:	Lab.objects.filter(patient=theCode).order_by('-created_date'),
		#'reports'			:	Reports.objects.filter(patient=code),
		'corpses'				:	corpses.objects.filter(patient_code=code),
		'payment'					:	Mpayment.objects.filter(patient=code)

	}
	return render(request, 'reception/patient_info.html', context)

def appointment_info(request,code):
	context={
	'appointment'	:	Appointment.objects.filter(patient=code).latest('-created_date'),
	}
	return render(request,'reception/appointment_details.html',context)

def payment_appointment_update(request, code, id):

	app_instance 	=	get_object_or_404(Appointment, patient=code, id=id)
	print(app_instance)
	update_apptmt_form 	= 	reception_forms.PaymentAppointmentStatusUpdate(request.POST or None, instance=app_instance.cashappointmentstatus)

	if request.method == 'POST':

		update_apptmt_form 	= 	reception_forms.PaymentAppointmentStatusUpdate(request.POST or None, instance=app_instance.cashappointmentstatus)

		if update_apptmt_form.is_valid():
			u_apptmt 				= 		update_apptmt_form.save(commit=False)
			u_apptmt.patient		=		request.POST.get('patient')
			update_apptmt_form.save()
			print('success')
			return redirect('reception:patient-info', code=u_apptmt.patient)

		else:
			print('not valid')

	else:

		update_apptmt_form 	= 	reception_forms.PaymentAppointmentStatusUpdate(instance=app_instance.cashappointmentstatus)

	context = {
		'update_apptmt_form' 		: 	update_apptmt_form,
		'appointment' 				: 	Appointment.objects.filter(patient=code, id=id),
	}

	return render(request, 'reception/payment_appointment_update.html', context)


def MorturyPayment(request, code):
	if request.method =='POST':
		MorturyPayment = reception_forms.MorturyPaymentUpdate(request.POST or None)

		if MorturyPayment.is_valid():
			if Mpayment.objects.filter(patient=code).exists():

				return redirect('reception:patient-info', code=code)
			else:
				pay=MorturyPayment.save(commit=False)
				pay.patient		=		request.POST.get('patient')
				pay.save()
				return redirect('reception:patient-info', code=code)
	MorturyPayment =reception_forms.MorturyPaymentUpdate()
	context ={

			'MorturyPayment'			:	MorturyPayment,
			'corpses'					:	corpses.objects.filter(patient_code=code),
			'payment'					:	Mpayment.objects.filter(patient=code)

	}
	return render(request, 'reception/morturyPayment.html', context)

def payment_lab_update(request, code, id):

	lab_instance 	=	get_object_or_404(Lab, patient=code, id=id)
	print(lab_instance)
	update_lab_form		=	reception_forms.PaymentLabStatusUpdate(request.POST or None, instance=lab_instance.cashlabstatus)

	if request.method == 'POST':

		update_lab_form		=	reception_forms.PaymentLabStatusUpdate(request.POST or None, instance=lab_instance.cashlabstatus)

		if update_lab_form.is_valid():
			u_lab 					=	update_lab_form.save(commit=False)
			u_lab.patient 			= 	request.POST.get('patient')
			#u_lab.totalPrice 			=	request.POST.get('totalPrice')
			update_lab_form.save()
			print('Success')
			return redirect('reception:patient-info', code=u_lab.patient)

		else:
			print('not valid')

	else:
		update_lab_form		=	reception_forms.PaymentLabStatusUpdate(instance=lab_instance.cashlabstatus)

	context = {
		'update_lab_form'		:	update_lab_form,
		'lab' 					: 	Lab.objects.filter(patient=code, id=id),
	}

	return render(request, 'reception/payment_lab_update.html', context)


def patient_invoices(request,code):



	comb 	=	combine_labs_appointments(code)
	context			={
	'all_payment':comb,
	'lab'	: CashLabStatus.objects.filter(status='Paid'),
	'apps'	: CashAppointmentStatus.objects.filter(status='Paid')
	}
	return render(request,'reception/patient_invoice.html',context)

def combine_labs_appointments(crud):
    labs = CashLabStatus.objects.filter(patient=crud)
    apps = CashAppointmentStatus.objects.filter(patient=crud)
    combined = sorted(
        chain(labs, apps),
        key=lambda c: c.status, reverse=False)
    return combined

def detailed_invoice(request,id):
	context={
	'lab'	: CashLabStatus.objects.filter(id=id),
	'apps'	: CashAppointmentStatus.objects.filter(id=id)
	}
	return render(request,'reception/detailed_invoice.html',context)

# def payment_pharmacy_update(request, code, id):
#
# 	pharmacy_instance 	=	get_object_or_404(InstructionsForPharmacy, patient=code, id=id)
# 	print(pharmacy_instance)
# 	update_pharmacy_form		=	reception_forms.PaymentPharmacyStatusUpdate(request.POST or None, instance=pharmacy_instance.pharmacylabstatus)
#
# 	if request.method == 'POST':
#
# 		update_pharmacy_form		=	reception_forms.PaymentPharmacyStatusUpdate(request.POST or None, instance=pharmacy_instance.pharmacylabstatus)
#
# 		if update_pharmacy_form.is_valid():
# 			update_pharmacy 			=	update_lab_form.save(commit=False)
# 			update_pharmacy.patient 	= 	request.POST.get('patient')
# 			#u_lab.totalPrice 			=	request.POST.get('totalPrice')
# 			update_pharmacy_form.save()
# 			print('Success')
# 			return redirect('reception:patient-info', code=update_pharmacy.patient)
#
# 		else:
# 			print('not valid')
#
# 	else:
# 		update_pharmacy_form		=	reception_forms.PaymentPharmacyStatusUpdate(instance=pharmacy_instance.pharmacylabstatus)
#
# 	context = {
# 		'update_pharmacy_form'		:	update_pharmacy_form,
# 		'pharmacy' 					: 	InstructionsForPharmacy.objects.filter(patient=code, id=id),
# 	}
#
# 	return render(request, 'reception/payment_pharmacy_update.html', context)
