from django.shortcuts import render,redirect
from reception.models import Patient
from mortury.models import corpses,Mpayment
# Create your views here.


def scancode(request):
    if request.method=='POST':
        thecode=request.POST.get('theCode',False)

        context={
        'patient'   : Patient.objects.filter(code=thecode),
        }
        return redirect('mortury:deadpatient',code=thecode)
    return render(request,'scan.html')

def deadpatient(request,code):

    context={
    'patient'   :   Patient.objects.filter(code=code),
    'status'    :   corpses.objects.filter(patient_code=code),
    'paid'      :   Mpayment.objects.filter(status='Paid'),
    }


    return render(request,'dead_patient.html',context)

def list(request):
    context={
    'deadPatient'   :   corpses.objects.all(),
    }
    return render(request,'list.html',context)
