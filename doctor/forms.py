from django import forms
from .models import Doctor,Reports,InstructionsForPharmacy,InstructionsForNurse
from django.forms import ValidationError
from django.forms import ModelForm
from reception.models import Lab
from mortury.models import corpses


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
    report        =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text','style':'height:100px;width:40%'}))

    class Meta:
        model   =   Reports
        fields  =('report',)

class AddPharmacyForm(forms.ModelForm):
    instructions       =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text','style':'height:100px;width:40%'}))

    class Meta:
        model   =   InstructionsForPharmacy
        fields  =('instructions',)

class AddIntensiveCareForm(forms.ModelForm):
    instructions        =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text','style':'height:100px;width:40%'}))

    class Meta:
        model   =   InstructionsForNurse
        fields  =('instructions',)

class AddDeathReport(forms.ModelForm):

    death_report          =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text','style':'height:100px;width:40%'}))
    date_of_death   =   forms.CharField(max_length=1000,
							widget=forms.TextInput(attrs={'name'	: 	'dob',
														  'class'	:	'form-control',
														  'type'	:	'date',
														  'placeholder':'Date of death',
                                                          'style':'width:40%'
														   }))

    class Meta:

        model   =   corpses
        fields  =   ('death_report','date_of_death')
