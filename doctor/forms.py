from django import forms
from .models import Doctor,Reports,InstructionsForPharmacy,InstructionsForNurse,Room,Allotment,Symptoms
from django.forms import ValidationError
from django.forms import ModelForm
from reception.models import Lab
from mortury.models import corpses
from django.forms import modelformset_factory

class AddDoctorForm(forms.ModelForm):
    firstname = forms.CharField(max_length=100,widget=forms.TextInput(attrs=
                                                                        {'name':'name','class':'form-control','type':'text','placeholder':'Enter first name',}))
    lastname = forms.CharField(max_length=100,widget=forms.TextInput(attrs=
                                                                        {'name':'name','class':'form-control','type':'text','placeholder':'Enter last name',}))
    gender = forms.ChoiceField(choices=[('Male', 'Male'),('Female', 'Female')],widget=forms.Select(attrs={	'class'	:	'form-control', }))
    email = forms.CharField(max_length=100,widget=forms.TextInput(attrs=
                                                                        {'name':'name','class':'form-control','type':'text','placeholder':'Enter mail',}))
    phone = forms.CharField(max_length=100,widget=forms.TextInput(attrs=
                                                                        {'name':'name','class':'form-control','type':'text','placeholder':'Enter phone',}))
    speciality = forms.CharField(max_length=100,widget=forms.TextInput(attrs=
                                                                        {'name':'name','class':'form-control','type':'text','placeholder':'Enter speciality',}))


    class Meta:
        model=Doctor
        fields=('firstname','lastname','gender','email','phone','speciality')

        def clean_email(self):
            email=self.cleaned_data.get('email')


class AddReportsForm(forms.ModelForm):
    diagnosis        =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text','placeholder':'Diagnosis'}))
    report        =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text','style':'height:50px;','placeholder':'Details'}))

    class Meta:
        model   =   Reports
        fields  =('diagnosis','report',)

class AddPharmacyForm(forms.ModelForm):
    instructions       =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text'}))
    drug_name       =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text'}))
    days       =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text'}))

    class Meta:
        model   =   InstructionsForPharmacy
        fields  =('instructions','drug_name','days')

class AddIntensiveCareForm(forms.ModelForm):
    instructions        =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text'}))

    class Meta:
        model   =   InstructionsForNurse
        fields  =('instructions',)

class AddRoomForm(forms.ModelForm):
    number      =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text'}))
    type        =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text'}))

    class Meta:
        model   =   Room
        fields  =   ('number','type')

class AddDeathReport(forms.ModelForm):

    death_report          =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text'}))
    date_of_death   =   forms.CharField(max_length=1000,
							widget=forms.TextInput(attrs={'name'	: 	'dob',
														  'class'	:	'form-control',
														  'type'	:	'date',
														  'placeholder':'Date of death',

														   }))

    class Meta:

        model   =   corpses
        fields  =   ('death_report','date_of_death')

SymptomsFormset = modelformset_factory(
    Symptoms,
    fields=('symptoms', ),
    extra=1,
    widgets={'name': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Book Name here'
        })
    }
)
