from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Doctor,Reports,Room,Allotment
from django.views.generic import CreateView, DetailView, UpdateView, DetailView, ListView
from . import forms as doctor_forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from reception.models import Patient,Lab,Appointment,CashAppointmentStatus
from mortury.models import corpses
from account.forms import UserUpdateForm
from reception.forms import AddLabForm
from Laboratory.models import Results
from django.contrib import messages
from ward.models import PatientStatus



# Create your views here.

# def doctor_home(request):
#
# 	return render(request, 'doctor/doc_home.html',{})

def patient(request,code):
	theCode=code

	if request.method =='POST':
		add_reports		=doctor_forms.AddReportsForm(request.POST or None)
		if add_reports.is_valid():
			report	=add_reports.save(commit=False)
			report.patient=request.POST.get('patient')
			print(report.patient)
			appointmentId	=	request.POST.get('appointmentId')
			print(appointmentId)
			c=Appointment.objects.filter(id=appointmentId)
			for c in c:
				report.appointment= c
				print(report.appointment)
				add_reports.save()
			context = {
				'reports'			:	Reports.objects.filter(patient=theCode, appointment=c),
				'scanCode'			:	Patient.objects.filter(code=theCode),
			}
			return render(request,'doctor/patient2.html' ,context)
	else:
		add_reports	=	doctor_forms.AddReportsForm()
		context	= {
		'scanCode'			:	Patient.objects.filter(code=theCode),
		'tests'				:	Lab.objects.filter(patient=theCode).order_by("-created_date"),
		'history'			:	Appointment.objects.filter(patient=theCode).order_by("-created_date"),
		# 'reports'			:	Reports.objects.filter(patient=theCode),
		'reportss':				add_reports,
		'results'			:	Results.objects.filter(patient=theCode),
		'status'			:	CashAppointmentStatus.objects.all(),
		'onGoing'			:	Appointment.objects.filter(patient=theCode).latest('created_date'),
		'deceased'			:	corpses.objects.filter(patient_code=theCode),

		}
	return render(request,'doctor/patient2.html',context)

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		if u_form.is_Valid():
			u_form.save()
			messages.SUCCESS(request,f'Updated successfully')
			return redirect('profile')
	else:
		u_form = UserUpdateForm(instance=request.user)
		context ={
		'u_form':u_form,
		}
	return render(request,'doctor/profile.html',context)

class AddDoctorView(LoginRequiredMixin, CreateView):
	form_class = doctor_forms.AddDoctorForm()
	template_name = 'doctor/add_doctor.html'
	model = Doctor

	def form_valid(self, form):
		doc =form.save(commit=False)
		doc.user=self.request.user
		docCheck= doctor.objects.filter(firstname=self.request.POST['firstname'],lastname=self.request.POST['lastname'])
		if docCheck:
			messages.add_message(self.request, messages.WARNING, f'Doctor With this Name Exist!')
			return redirect('doctor:add_doctor')
		else:
			doc.save()
			messages.add_message(self.request, messages.SUCCESS, f'doctor Created successfully')

		return redirect('doctor:add_doctor')


#@login_required(login_url='/')
def ScanCode(request):

	if request.method =='POST':
		theCode 		= 	request.POST.get('theCode', False)
		print(theCode)
		add_reports		=doctor_forms.AddReportsForm(request.POST or None)
		return redirect('doctor:patient',code=theCode)
	# context={
	#  'scanCode'				:	Patient.objects.filter(code=theCode),
	#  }

	return render(request, 'doctor/doc_home.html')

@login_required(login_url='/')
def patient_lab_test(request, code):
	if request.method =='POST':
		lab_test = AddLabForm(request.POST or None)

		if lab_test.is_valid():
			lab= lab_test.save(commit=False)
			lab.patient=request.POST.get('patient')
			lab.totalPrice 			=	request.POST.get('totalPrice')
			lab_test.save()
			return redirect('doctor:ScanCode')
	lab_test = AddLabForm()
	context ={
			'patientInfo'			:	Patient.objects.filter(code=code),
			'add_lab_form'			:	lab_test,
			'reports'				:	Reports.objects.filter(patient=code),
	}
	return render(request,'doctor/patient_lab_test.html',context)


def send_for_pharmacy(request,code):
	if request.method =='POST':
		send_for_pharmacy = doctor_forms.AddPharmacyForm(request.POST or None)

		if send_for_pharmacy.is_valid():
			phar= send_for_pharmacy.save(commit=False)
			phar.patient=request.POST.get('patient')
			print(phar.patient)
			phar.save()
			return redirect('doctor:patient',code=phar.patient)

	send_for_pharmacy = doctor_forms.AddPharmacyForm()
	context ={
			'patientInfo'			:	Patient.objects.filter(code=code),
			'reports'				:	Reports.objects.filter(patient=code),
			'addInstructions'		:	 doctor_forms.AddPharmacyForm(),
	}

	return render(request,'doctor/send_for_pharmacy.html',context)

def send_for_icu(request,code):
	if request.method =='POST':
		send_for_icu = doctor_forms.AddIntensiveCareForm(request.POST or None)

		if send_for_icu.is_valid():
			phar= send_for_icu.save(commit=False)
			phar.patient=request.POST.get('patient')
			phar.save()
			return redirect('doctor:patient',code=phar.patient)

	send_for_icu = doctor_forms.AddIntensiveCareForm()
	context ={
	'patientInfo'			:	Patient.objects.filter(code=code),
	'reports'				:	Reports.objects.filter(patient=code),
			'addInstructions'		:	 doctor_forms.AddIntensiveCareForm(),
	}

	return render(request,'doctor/send_for_icu.html',context)

def AddDeathReport(request,code):
	if request.method=='POST':
		death_report= doctor_forms.AddDeathReport(request.POST or None)

		if death_report.is_valid():
			report=death_report.save(commit=False)
			report.patient_code=code
			report.patient=request.POST.get('patient')
			print(report.patient)
			report.save()
		return redirect('doctor:patient',code=report.patient_code)
	death_report	=	doctor_forms.AddDeathReport()
	context={
	'patient' 	:		Patient.objects.filter(code=code),
	'd_form'	:		death_report,
	}
	return render(request,'doctor/adddeathreport.html',context)



def reports(request,code,id):

	report_instance = get_object_or_404(Appointment,patient=code,id=id)
	updateReports = doctor_forms.AddReportsForm(request.POST or None,instance=report_instance.reports)
	print(report_instance)

	if request.method=='POST':

		updateReports = doctor_forms.AddReportsForm(request.POST or None,instance=report_instance.reports)


		if updateReports.is_valid():
			report			=		updateReports.save(commit=False)
			report.patient	=		code
			report.save()
			messages.success(request, 'Report saved successfully.')
			return redirect('doctor:patient',code=report.patient)
		else:
			print('its not working man')
	else:
		updateReports = doctor_forms.AddReportsForm(instance=report_instance.reports)
	context={
				'add_report'		:	updateReports,
				'appointment'		:	Appointment.objects.filter(patient=code,id=id),
				'patient'			:	Patient.objects.filter(code=code)
	}
	return render(request,'doctor/reports.html',context)


def C_reports(request,code,id):
	context={
	'reports'	:	Reports.objects.filter(patient=code,appointment_id=id),
	}
	return render(request,'doctor/theReport.html',context)

def C_results(request,code,id):
	print('im seeing the page')
	theCode=code
	theId=id
	context={
	'results'	:Results.objects.filter(patient=code,tests_id=theId),
	}
	return render(request,'doctor/theResult.html',context)


def inPatient(request):

	context={
	'inpatients'	:	PatientStatus.objects.filter(status='InPatient'),
	}
	return render(request,'doctor/InPatient.html',context)

def outPatient(request):

	context={
	'Outpatients'	:	PatientStatus.objects.filter(status='OutPatient'),
	}
	return render(request,'doctor/OutPatient.html',context)

def addRoom(request):
	if request.method == "POST":
		addR	=	doctor_forms.AddRoomForm(request.POST or none)

		if addR.is_valid():
			addR.save()
			messages.success(request,f'Added successfully')
			return redirect('doctor:addRoom')
	addRoom= doctor_forms.AddRoomForm()
	context={
	'addRoom':addRoom
	}
	return render(request,'doctor/addRoom.html',context)

def allRooms(request):
	context={
	'allRooms'	:	Room.objects.all(),
	}
	return render(request,'doctor/allRooms.html',context)
