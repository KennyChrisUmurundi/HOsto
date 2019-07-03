import json
from django import forms
from django.forms import ValidationError
from django.forms import ModelForm
#from crispy_forms.layout import Field
from .models import Patient, Appointment, Lab, CashAppointmentStatus, CashLabStatus
from doctor.models import Category, Doctor
# from .choices import TESTS, CATEGORIES, DOCTORS
#from phone_field import PhoneField

class AddPatientForm(forms.ModelForm):

	firstname = forms.CharField(max_length=100,
							widget=forms.TextInput(attrs={'name'	: 	'name',
														  'class'	:	'form-control',
														  'type'	:	'text',
														  'placeholder':'Enter Patient First Name', }))

	lastname = forms.CharField(max_length=1000,
							widget=forms.TextInput(attrs={'name'	: 	'description',
														  'class'	:	'form-control',
														  'type'	:	'text',
														  'placeholder':'Enter Patient Last Name', }))
	dob		 =	forms.CharField(max_length=1000,
							widget=forms.TextInput(attrs={'name'	: 	'dob',
														  'class'	:	'form-control',
														  'type'	:	'date',
														  'placeholder':'Enter Patient Last Name',
														  'onchange' 	:	'submitBday()', }))

	status   = forms.ChoiceField(choices=[('single', 'Single'),('Married', 'Married')],
								widget=forms.RadioSelect(attrs={'style' : 'font-size: 20px;'}))

	medical_history = forms.CharField(max_length=200,
							widget=forms.Textarea(attrs={'name'			: 	'medical_history',
														  'class'		:	'form-control',
														  'type'		:	'Textarea',
														  'rows'		:	'3',
														  'placeholder'	:	'Enter Medical History of the Patient', }))


	age = forms.CharField(max_length=200,
							widget=forms.TextInput(attrs={'name'		: 	'age',
														  'class'		:	'form-control',
														  'type'		:	'text',
														  'placeholder'	:	'Patient Age',
														  'style'		:	'color: black',
														  'readonly'	:	'true', }))


	address = forms.CharField(max_length=200,
							widget=forms.Textarea(attrs={'name'			: 	'address',
														  'class'		:	'form-control',
														  'type'		:	'Textarea',
														  'rows'		:	'3',
														  'placeholder'	:	'Enter Client Main address', }))

	gender = forms.ChoiceField(choices=[('Male', 'Male'),('Female', 'Female')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))

	phone = forms.CharField(max_length=200,
							widget=forms.TextInput(attrs={'name'	: 	'phone',
														  'class'	:	'form-control',
														  'type'	:	'text',
														  'placeholder':'Enter Patient Phone Number', }))


	email 		= 	forms.CharField(max_length=200,
							widget=forms.TextInput(attrs={'name'	: 	'email',
														  'class'	:	'form-control',
														  'type'	:	'text',
														  'placeholder':'Enter Patient Email', }))
	occupation 	= 	forms.CharField(max_length=200,
							widget=forms.TextInput(attrs={'name'	: 	'occupation',
														  'class'	:	'form-control',
														  'type'	:	'text',
														  'placeholder':'Enter Patient Occupation', }))

	payment 	= 	forms.ChoiceField(choices=[('Cashless', 'Cashless'),('Cash', 'Cash')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))


	image 	= 	forms.CharField(max_length=200,
							widget=forms.TextInput(attrs={'name'	: 	'image',
														  'class'	:	'form-control',
														  'type'	:	'file',
														  'style'	:	'padding: 0px 0px 0px 0px;' }))


	class Meta:
		model = Patient
		fields = ('firstname', 'lastname', 'gender', 'phone', 'dob', 'age', 'status', 'medical_history', 'address','email', 'occupation','payment', 'image')

		def clean_email(self):
			email = self.cleaned_data.get('email')

class AddAppointmentForm(forms.ModelForm):

	docZ = {}
	list_doctors = []
	for doc_info in Doctor.objects.all():
		if doc_info.category.name in docZ:
			docZ[doc_info.category.name].append(doc_info.name)
		else:
			docZ[doc_info.category.name] = [doc_info.name]
		list_doctors.append((doc_info.name, doc_info.name))

	#category = Category.objects.all()
	categories = [str(category) for category in Category.objects.all()]


	category_select = forms.ChoiceField(label='Doctor Category', choices=([(category, category) for category in categories]),
							widget=forms.Select(attrs={	'class'		:	'form-control',
														'id'		:	'category',
														'disabled'	:	'true' }))

	doctor_select = forms.ChoiceField(label='Doctor', choices=(list_doctors),
							widget=forms.Select(attrs={	'class'		:	'form-control',
														'id'		:	'id_doctor',
														'disabled'	:	'true', }))

	categories 	= 	json.dumps(categories)
	doctors 	=	json.dumps(docZ)


	class Meta:
		model = Appointment
		fields = ('category_select', 'doctor_select')

	def __init__(self, *args, **kwargs):
		super(AddAppointmentForm, self).__init__(*args, **kwargs)
		self.fields['category_select'].required = False
		self.fields['doctor_select'].required = False



class AddLabForm(forms.ModelForm):

	# test_category = forms.ChoiceField(choices=[('', 'Select Test'),('Maleria', 'Maleria'),('Typhoid', 'Typhoid')],
	# 						widget=forms.Select(attrs={	'class'	:	'form-control',
	# 													'id'	:	'test_category' }))

	tests = forms.CharField(max_length=200,
							widget=forms.Textarea(attrs={'name'			: 	'tests',
														  'class'		:	'form-control',
														  'type'		:	'Textarea',
														  'rows'		:	'4',
														  'readonly'	:	'True',
														  'placeholder'	:	'Here Goes Patient Tests', }))

	# test_category = forms.ChoiceField(choices=TESTS,
	# 									widget=forms.Select(attrs={'name'	:	'test_cat',
	# 															   'class' 	: 'form-control', }))
	totalPrice = forms.CharField(max_length=200,
									widget=forms.TextInput(attrs={'name'		:	'totalPrice',
															  	  'class'		:	'form-control',
															  	  'readonly'	:	'True',
															  	  'placeholder'	:	'Here goes Total Test Price'}))
	class Meta:
		model 	= 	Lab
		fields	=	('tests',)

	def __init__(self, *args, **kwargs):
		super(AddLabForm, self).__init__(*args, **kwargs)
		self.fields['tests'].required = False

class PaymentAppointmentStatusUpdate(forms.ModelForm):
	status = forms.ChoiceField(choices=[('', 'Select Status of the Payment'),('Paid', 'Paid'),('Unpaid', 'Unpaid')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))
	class Meta:
		model 	=	CashAppointmentStatus
		fields	=	['status']

class PaymentLabStatusUpdate(forms.ModelForm):
	status = forms.ChoiceField(choices=[('', 'Select Status of the Payment'),('Unpaid', 'Unpaid'),('Paid', 'Paid')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))
	class Meta:
		model 	=	CashLabStatus
		fields	=	['status']

# class PaymentPharmacyStatusUpdate(forms.ModelForm):
# 	status = forms.ChoiceField(choices=[('', 'Select Status of the Payment'),('Unpaid', 'Unpaid'),('Paid', 'Paid')],
# 							widget=forms.Select(attrs={	'class'	:	'form-control', }))
# 	class Meta:
# 		model 	=	CashPharmacyStatus
# 		fields	=	['status']
