from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from doctor.models import InstructionsForPharmacy
from reception.models import Patient
from . import forms as pharmacy_forms
from django.contrib import messages
from .models import Drugs,TakenDrugs
from django.db.models import Sum
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf
import datetime
# Create your views here.

def scanBarcode(request):
    if request.method=='POST':
        code =  request.POST.get('theCode',False)
        print(code)
        return redirect('pharmacy:patient',code=code)

    return render(request,'scanBarcode.html')


def pharmacy_patient(request,code):

    context={
    'prescription'  :   InstructionsForPharmacy.objects.filter(patient=code).order_by("-created_date"),
    'patientInfo': Patient.objects.filter(code=code),
    }
    return render(request,'check_prescriptions.html',context)


def drugs(request,code):
    context={
    'prescription'  :   InstructionsForPharmacy.objects.filter(patient=code).order_by("-created_date"),
    'drugs'         :   Drugs.objects.all(),
    'patientInfo'   :      Patient.objects.filter(code=code),
    }

    return render(request,'drugs.html',context)

def drugsList(request):
    context={
    'drugs'         :   Drugs.objects.all(),
    }

    return render(request,'DrugList.html',context)


def add_drugs(request):

    if request.method=='POST':
        add_drugs =   pharmacy_forms.AddDrugsForm(request.POST or None)

        if add_drugs.is_valid():
            drug=add_drugs.save(commit=False)
            drug.save()
            messages.success(request,f'Added successfully')
            return redirect('pharmacy:add_drugs')
    else:
        add_drugs=pharmacy_forms.AddDrugsForm()
        context={
            'add_drugs'     :   add_drugs,
        }
    return render(request, 'add_drugs.html', context)


def confirm_drug_payment(request,code,id):

    if request.method=='POST':
        add_drugs_payment =   pharmacy_forms.AddTakenDrugsForm(request.POST or None)

        if add_drugs_payment.is_valid():
            drug=add_drugs_payment.save(commit=False)
            drug.patient=request.POST.get('patient')
            quantity=request.POST.get('quantity')
            theQuantity= int('0'+quantity)
            print(theQuantity)
            unitPrice=Drugs.objects.values_list('pricePerUnit', flat=True).filter(id=id)
            for unitPrice in unitPrice:
                unitPrice=int('0'+unitPrice)
                print(unitPrice)
            totalPrice=theQuantity*unitPrice
            print(totalPrice)



            drug.drugName= request.POST.get('DrugName')
            drug.totalPrice=totalPrice
            print(drug.drugName)
            drug.save()
            # messages.success(request,f'Added successfully')
            return redirect('pharmacy:drugs',code=drug.patient)
    else:
        add_drugs_payment=pharmacy_forms.AddTakenDrugsForm()
        context={
            'add_drugs_payment'     :   add_drugs_payment,
            'confirm_drug_payment'  :   TakenDrugs.objects.filter(patient=code,id=id),
            'patientInfo': Patient.objects.filter(code=code),
            'drug'       :  Drugs.objects.filter(id=id),

        }
    return render(request, 'ConfirmDrugPayment.html', context)


def invoice(request,code):
    date=datetime.date.today()
    totalDrugPrice=TakenDrugs.objects.filter(patient=code).aggregate(Sum('totalPrice'))['totalPrice__sum']
    context={
    'patientInfo': Patient.objects.filter(code=code),
    'takenDrugs' : TakenDrugs.objects.filter(patient=code,created_date=date),
    'totalDrugPrice' :totalDrugPrice
    }
    return render(request,'invoice.html',context)

def invoToPdf(request,code):
    date=datetime.date.today()
    totalDrugPrice=TakenDrugs.objects.filter(patient=code).aggregate(Sum('totalPrice'))['totalPrice__sum']
    context={
            'patientInfo': Patient.objects.filter(code=code),
                 'takenDrugs' : TakenDrugs.objects.filter(patient=code,created_date=date),
                 'totalDrugPrice' :totalDrugPrice
            }
    pdf = render_to_pdf('invoice.html',context)
    return HttpResponse(pdf,content_type='application/pdf')


# def pharmacy_patient(request,code,id):
#
#     context={
#     'prescription'  :   InstructionsForPharmacy.objects.filter(patient=code).order_by("-created_date"),
#     'patientInfo': Patient.objects.filter(code=code),InstructionsForPharmacy.objects.filter(patient=code,id=id)
#     'k'             :
#     }
#     return render(request,'check_prescriptions.html',context)
