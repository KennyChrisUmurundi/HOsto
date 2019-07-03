from django.shortcuts import render,redirect
from doctor.models import InstructionsForNurse
from reception.models import Patient
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
    'patientInfo': Patient.objects.filter(code=code),
	
    }
    return render(request,'patient.html',context)
