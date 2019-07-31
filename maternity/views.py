from django.shortcuts import render,redirect
from reception.models import Patient

# Create your views here.

def scancode(request):
    if request.method=='POST':
        thecode=request.POST.get('theCode',False)

        context={
        'patient'   : Patient.objects.filter(code=thecode),
        }
        return redirect('maternity:maternityPatient',code=thecode)
    return render(request,'maternityScan.html')

def maternityPatient(request,code):
    context={
    'patientInfo'   :   Patient.objects.filter(code=code)
    }
    return render(request,'maternityPatient.html',context)
