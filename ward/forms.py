from django import forms
from django.forms import ValidationError
from django.forms import ModelForm
from .models import PatientStatus, PatientReport

class PatientStatusUpdate(forms.ModelForm):
	prescription = forms.CharField(label='Prescription',required=False, widget=forms.Textarea(attrs={'name'			: 	'prescription',
														  		'class'			:	'form-control',
														  		'type'			:	'Textarea',
														  		'rows'			:	'7',
														  		'placeholder'	:	'Patient Ward Prescription', }))

	report = forms.CharField(label='report',required=False,widget=forms.Textarea(attrs={'name'			: 	'report',
														  		'class'			:	'form-control',
														  		'type'			:	'Textarea',
														  		'rows'			:	'7',
														  		'placeholder'	:	'Patient Ward Prescription', }))


	status = forms.ChoiceField(label='Status',required=False,choices=[('', 'Select Status of the Patient'),('InPatient', 'InPatient'),('OutPatient', 'OutPatient')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))
	class Meta:
		model 	=	PatientStatus
		fields	=	['status', 'prescription', 'report']

class PatientFinalReport(forms.ModelForm):
	doctor_prescription = forms.CharField(label='Prescription',required=False,widget=forms.Textarea(attrs={'name'			: 	'doctor_prescription',
														  		'class'			:	'form-control',
														  		'type'			:	'Textarea',
														  		'rows'			:	'7',
														  		'placeholder'	:	'Patient Ward Prescription', }))

	nurse_report = forms.CharField(label='Report',required=False,widget=forms.Textarea(attrs={'name'			: 	'report',
														  		'class'			:	'form-control',
														  		'type'			:	'Textarea',
														  		'rows'			:	'7',
														  		'placeholder'	:	'Patient Nurse Report', }))

	class Meta:
		model 	=	PatientReport
		fields	=	['doctor_prescription', 'nurse_report']
