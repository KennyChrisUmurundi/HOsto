from django.shortcuts import render,redirect
from doctor.models import InstructionsForNurse
from reception.models import Patient
from . import forms as icu_forms
# Create your views here.


def ScanCode(request):

	if request.method =='POST':
		theCode 		= 	request.POST.get('theCode', False)
		# context={
		# 'code'	:	Appointment.objects.filter(patient=theCode)
		# }
		return redirect('icu:patient',code=theCode)

	return render(request,'scanbarcode.html')

def patient(request,code):

    context={
    'instructions'  :   InstructionsForNurse.objects.filter(patient=code).order_by("-created_date"),
    'patientInfo':		 Patient.objects.filter(code=code),

    }
    return render(request,'patient.html',context)

def feedback(request,code,id):
	if request.method=='POST':
		f_form	=	icu_forms.AddFeedbackForm(request.POST or None)
		id=id
		code=code
		if f_form.is_valid():
			feedback	= f_form.save(commit=False)
			feedback.patient=code
			print(feedback.patient)
			feedback.Instructions_id=id
			feedback.save()
			return redirect('icu:patient',code=feedback.patient)
	else:
		f_form= icu_forms.AddFeedbackForm()
		context={
			'f_form':f_form,
			'instructions'  :   InstructionsForNurse.objects.filter(patient=code,id=id),
			'patient'		:	Patient.objects.filter(code=code),
		}
		return render(request,'feedback.html',context)
