from django.shortcuts import render,redirect, get_object_or_404
from django.shortcuts import render,redirect
from reception.models import Patient,Lab
from . import forms as lab_forms
from django.contrib import messages


def lab_scanBarcode(request):
    if request.method=='POST':
        code =  request.POST.get('theCode',False)
        print(code)

        context={
        'patient': Patient.objects.filter(code=code),
        # 'results':results,

        }
        return redirect('Laboratory:lab_patient',code=code)

    return render(request,'lab_scanBarcode.html')


def lab_patient(request,code):
    mycode=code
    print(mycode)
    if request.method=='POST':
        add_results =   lab_forms.AddResultsForm(request.POST or None)

        if add_results.is_valid():
            results=add_results.save(commit=False)
            results.patient= request.POST.get('patient')
            results.save()
            return redirect('Laboratory:lab_patient',code=code)
    else:
        add_results=lab_forms.AddResultsForm()
        context={
            'patientInfo'       : Patient.objects.filter(code=mycode),
            'tests'				:	Lab.objects.filter(patient=mycode).order_by("-created_date"),
            'results'            :add_results,
        }
    return render(request, 'lab_patient.html', context)

def perform_test(request,code,id):
    result_instance = get_object_or_404(Lab,patient=code,id=id)
    print(result_instance)
    updateResults = lab_forms.AddResultsForm(request.POST or None,instance=result_instance.results)
    test_status     =   lab_forms.AddTeststatusForm(request.POST or None,instance=result_instance.teststatus)

    if request.method=='POST':
        perform_theTest =   lab_forms.AddResultsForm(request.POST or None,instance=result_instance.results)
        test_status     =   lab_forms.AddTeststatusForm(request.POST or None,instance=result_instance.teststatus)## TODO: early morning update the test status...right now go sleep man!!The idea is,upon test prformed the status should update automatically,find a way!!
        if perform_theTest.is_valid() and test_status.is_valid():

            status=test_status.save(commit=False)
            status.patient=request.POST.get('patient')
            status.save()
            print('saved')

            results=perform_theTest.save(commit=False)
            results.patient= request.POST.get('patient')
            print(results.patient)

            results.save()

            return redirect('Laboratory:lab_patient',code=results.patient)
        # else:
        #     if test_status.is_valid():
        #
        #         status=test_status.save(commit=False)
        #         status.patient=request.POST.get('patient')
        #         print(status.status)
        #         status.save()

    else:
        perform_theTest=lab_forms.AddResultsForm(instance=result_instance.results)
        test_status     =   lab_forms.AddTeststatusForm(instance=result_instance.teststatus)
    context={
            'tests'				:	Lab.objects.filter(patient=code,id=id),
            'results'           :   perform_theTest,
            'status'            :   test_status,
            
    }

    return render(request,'perform_test.html',context)

def results(request,code,id):
    context={
    'theResults':Results.objects.filter(patient=code,test_id=id)
    }
    return render(request,'results.html'/context)
