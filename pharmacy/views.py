from django.shortcuts import render,redirect, get_object_or_404,HttpResponseRedirect
from django.http import HttpResponse,JsonResponse
from doctor.models import InstructionsForPharmacy
from reception.models import Patient
from . import forms as pharmacy_forms
from django.contrib import messages
from .models import Drugs,TakenDrugs,Category,DrugsSupplier
from django.db.models import Sum
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf
import datetime
from datetime import date
from datetime import timedelta
from django.shortcuts import render_to_response
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

def dashboard(request):
    Total=Drugs.objects.all().count(),
    Out=Drugs.objects.filter(quantity='0').count(),
    labels=["Drugs","Out Of Stock","Expired"]
    default=[Total,20,20]
    data={
    'total'         :   Drugs.objects.all().count(),
    'totalSale'     :   TakenDrugs.objects.all().aggregate(Sum('totalPrice'))['totalPrice__sum'],
    'outofstock'    :   Drugs.objects.filter(quantity='0').count(),
    'labels'        :   labels,
    'default'       :   default,
    }
    return render(request,'Dashboard.html',data)


def get_data(request,*args,**kwargs):

    data ={
    'medecine'  :   Drugs.objects.all().count(),
    }
    return JsonResponse(data)

def scanBarcode(request):
    if request.method=='POST':
        code =  request.POST.get('theCode',False)
        print(code)
        return redirect('pharmacy:drugs',code=code)

    return render(request,'scanBarcode.html')


def pharmacy_patient(request,code):

    context={
    'prescription'  :   InstructionsForPharmacy.objects.filter(patient=code).order_by("-created_date"),
    'patientInfo': Patient.objects.filter(code=code),
    }
    return render(request,'check_prescriptions.html',context)


def drugs(request,code):
    drugs_list  =  Drugs.objects.all()
    if request.method == 'POST':
        name 		= 	request.POST.get('name', False)
        print(name)
        context = {
        'drugss'			:	Drugs.objects.filter(name__icontains=name),
        'patientInfo'   :      Patient.objects.filter(code=code),
        }
        return render(request,'drugs.html',context)
    paginator   = Paginator(drugs_list,10)
    page =request.GET.get('page')
    try:
        drugs_list  =   paginator.page(page)
    except PageNotAnInteger:
        drugs_list  =   paginator.page(1)
    except EmptyPage:
        drugs_list  =   paginator.page(paginator.num_pages)
    context={
    'prescription'  :   InstructionsForPharmacy.objects.filter(patient=code).order_by("-created_date"),
    'drugs'         :   drugs_list,
    'patientInfo'   :      Patient.objects.filter(code=code),
    }

    return render(request,'drugs.html',context)

def drugsList(request):
    drugs_list  =  Drugs.objects.all()
    umuti   =   Drugs.objects.filter(id=28)## temporary stuff

    if request.method == 'POST':
        name 		= 	request.POST.get('name', False)
        print(name)
        context = {
        'drugss'			:	Drugs.objects.filter(name__icontains=name),
        }
        return render(request,'DrugList.html',context)

    paginator   = Paginator(drugs_list,10)
    page =request.GET.get('page')
    try:
        drugs_list  =   paginator.page(page)
    except PageNotAnInteger:
        drugs_list  =   paginator.page(1)
    except EmptyPage:
        drugs_list  =   paginator.page(paginator.num_pages)
    context={
    'drugs'         :   drugs_list,
    'today'         :datetime.date.today(),


    }

    return render(request,'DrugList.html',context)

def categoryList(request):
    context={
    'categoryList'  :   Category.objects.all(),
    }
    return render(request,'categoryList.html',context)

def suppliersList(request):
    context={
    'suppliersList'  :   DrugsSupplier.objects.all(),
    }
    return render(request,'suppliersList.html',context)


def add_drugs(request):

    storage =   messages.get_messages(request)

    if request.method=='POST':
        add_drugs =   pharmacy_forms.AddDrugsForm(request.POST or None)

        if add_drugs.is_valid():
            add_drugs.save()
            print('ik')
            messages.success(request,f'Added successfully')
            return redirect('pharmacy:add_drugs')

    add_drugs=pharmacy_forms.AddDrugsForm()
    context={
            'add_drugs'     :   add_drugs,
            'message'       :   storage
    }
    return render(request, 'add_drugs.html', context)

def add_drugsCa(request):

    if request.method=='POST':
        add_drugsC =   pharmacy_forms.AddDrugsCForm(request.POST or None)

        if add_drugsC.is_valid():
            add_drugsC.save()
            print('ik')
            messages.success(request,f'Added successfully')
            return redirect('pharmacy:add_drugs')

    add_drugsC=pharmacy_forms.AddDrugsCForm()
    context={
            'add_drugsC'     :   add_drugsC,
    }
    return render(request, 'add_drugsCategory.html', context)


def add_drugsSupplier(request):

    if request.method=='POST':
        add_drugsS =   pharmacy_forms.AddDrugsSupplierForm(request.POST or None)

        if add_drugsS.is_valid():
            add_drugsS.save()
            print('ik')
            messages.success(request,f'Added successfully')
            return redirect('pharmacy:add_drugs')

    add_drugsS=pharmacy_forms.AddDrugsSupplierForm()
    context={
            'add_drugsSupplier'     :   add_drugsS,
    }
    return render(request, 'add_drugsSupplier.html', context)





def confirm_drug_payment(request,code,id):

    if request.method=='POST':
        add_drugs_payment =   pharmacy_forms.AddTakenDrugsForm(request.POST or None)

        if add_drugs_payment.is_valid():
            drug=add_drugs_payment.save(commit=False)
            drug.patient=request.POST.get('patient')
            quantity=request.POST.get('quantity')
            remainingDrugs  =   Drugs.objects.filter(id=id)
            for rem in remainingDrugs:
                remainder   =   rem.quantity
                print(remainder)
                if quantity < remainder or quantity == remainder:
                    print('its less')
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
                    messages.success(request,f'Added successfully')
                    intRemainder    =   int('0'+remainder)
                    newValue = intRemainder-theQuantity
                    Drugs.objects.filter(id=id).update(quantity=newValue)
                    return redirect('pharmacy:drugs',code=drug.patient)
                else:
                    messages.warning(request,f'Quantity Surpasses Stock')
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
    totalDrugPrice=TakenDrugs.objects.filter(patient=code,created_date=date).aggregate(Sum('totalPrice'))['totalPrice__sum']
    context={
    'patientInfo': Patient.objects.filter(code=code),
    'takenDrugs' : TakenDrugs.objects.filter(patient=code,created_date=date),
    'totalDrugPrice' :totalDrugPrice
    }
    return render(request,'invoice.html',context)

def invoToPdf(request,code):
    date=datetime.date.today()
    totalDrugPrice=TakenDrugs.objects.filter(patient=code,created_date=date).aggregate(Sum('totalPrice'))['totalPrice__sum']
    context={
            'patientInfo': Patient.objects.filter(code=code),
                 'takenDrugs' : TakenDrugs.objects.filter(patient=code,created_date=date),
                 'totalDrugPrice' :totalDrugPrice
            }
    pdf = render_to_pdf('invoice.html',context)
    return HttpResponse(pdf,content_type='application/pdf')


def deleteCategory(request,id):

    object  =   get_object_or_404(Category,id=id)
    object.delete()
    return redirect('pharmacy:categoryList')

def deleteDrug(request,id):

    object  =   get_object_or_404(Drugs,id=id)
    object.delete()
    messages.success(request,f'Deleted successfully')
    return redirect('pharmacy:drugsList')

def editCategory(request,id):

    object  =   get_object_or_404(Category,id=id)

    if request.method=='POST':
        add_drugsC =   pharmacy_forms.AddDrugsCForm(request.POST,instance=object)

        if add_drugsC.is_valid():
            add_drugsC.save()
            return redirect('pharmacy:categoryList')

    add_drugsC=pharmacy_forms.AddDrugsCForm(instance=object)
    context={
            'add_drugsC'     :   add_drugsC,
    }
    return render(request, 'editCategory.html', context)

def editSupplier(request,id):

    object  =   get_object_or_404(DrugsSupplier,id=id)

    if request.method=='POST':
        add_drugsS =   pharmacy_forms.AddDrugsSupplierForm(request.POST,instance=object)

        if add_drugsS.is_valid():
            add_drugsS.save()
            print('ik')
            messages.success(request,f'Added successfully')
            return redirect('pharmacy:add_drugs')

    add_drugsS=pharmacy_forms.AddDrugsSupplierForm(instance=object)
    context={
            'add_drugsSupplier'     :   add_drugsS,
    }
    return render(request, 'editSupplier.html', context)

def editDrugs(request,id):

    object  =   get_object_or_404(Drugs,id=id)

    if request.method=='POST':
        add_drugs =   pharmacy_forms.AddDrugsForm(request.POST,instance=object)

        if add_drugs.is_valid():
            add_drugs.save()
            print('ik')
            messages.success(request,f'Updated successfully')
            return redirect('pharmacy:add_drugs')

    add_drugs=pharmacy_forms.AddDrugsForm(instance=object)
    context={
            'add_drugs'     :   add_drugs,
    }
    return render(request, 'add_drugs.html', context)

def outofstock(request):
    context={
    'outofstock'    :   Drugs.objects.all()
    }
    return render(request,'OutOfStock.html',context)

def loadStock(request,id):

    object  =   get_object_or_404(Drugs,id=id)

    if request.method=="POST":
        load_drug   =   pharmacy_forms.LoadOutofStock(request.POST,instance=object)

        if load_drug.is_valid():
            load_drug.save()
            messages.success(request,f'Loaded successfully')
            return redirect('pharmacy:OutOfStock')
    load_drug=pharmacy_forms.LoadOutofStock(instance=object)
    context={
    'load_drug' :   load_drug,
    'Drug'      :   Drugs.objects.filter(id=id),
    }
    return render(request,'load_drug.html',context)

def expiredDrugs(request):
    context={
    'expired'   :   Drugs.objects.all(),
    'today'         :datetime.date.today(),
    }
    return render(request,'expired_drugs.html',context)
