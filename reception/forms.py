import json
from django import forms
from django.forms import ValidationError
from django.forms import ModelForm
#from crispy_forms.layout import Field
from .models import Patient, Appointment, Lab, CashAppointmentStatus, CashLabStatus
from doctor.models import Category, Doctor, Prices
from mortury.models import Mpayment
# from .choices import TESTS, CATEGORIES, DOCTORS
#from phone_field import PhoneField

class AddPatientForm(forms.ModelForm):

	firstname = forms.CharField(max_length=100,
							widget=forms.TextInput(attrs={'name'	: 	'name',
														  'class'	:	'form-control',
														  'type'	:	'text',
														  'placeholder':'Patient First Name',

														   }))

	lastname = forms.CharField(max_length=100,
							widget=forms.TextInput(attrs={'name'	: 	'description',
														  'class'	:	'form-control',
														  'type'	:	'text',
														  'placeholder':'Enter Patient Last Name', }))
	dob		 =	forms.CharField(max_length=1000,
							widget=forms.TextInput(attrs={'name'	: 	'dob',
														  'class'	:	'form-control',
														  'type'	:	'date',
														  'onchange' 	:	'submitBday()', }))

	status   = forms.ChoiceField(choices=[('single', 'Single'),('Married', 'Married')],
								widget=forms.Select(attrs={'class'	:	'form-control',}))

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
														  'type'	:	'tel',
														  'placeholder':'', }))


	email 		= 	forms.EmailField(required=False,widget=forms.TextInput(attrs={'name'	: 	'email',
														  'class'	:	'form-control',
														  'type'	:	'text',
														  'placeholder':'Enter Patient Email', }))
	occupation 	= 	forms.CharField(max_length=200,
							widget=forms.TextInput(attrs={'name'	: 	'occupation',
														  'class'	:	'form-control',
														  'type'	:	'text',
														  'placeholder':'Enter Patient Occupation', }))

	payment 	= 	forms.ChoiceField(choices=[('Credit Card', 'Credit Card'),('Cash', 'Cash'),('Insurance', 'Insurance')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))


	image 	= 	forms.CharField(max_length=200,required=False,
							widget=forms.TextInput(attrs={'name'	: 	'image',
														  'class'	:	'form-control',
														  'type'	:	'file',
														  'style'	:	'padding: 0px 0px 0px 0px;' }))



	patient_identification= forms.CharField(max_length=100,
							widget=forms.TextInput(attrs={'name'	: 	'patient_id',
														  'class'	:	'form-control',
														  'type'	:	'text',
														  'placeholder':'Patient ID', }))





	class Meta:
		model = Patient
		fields = ('firstname', 'lastname', 'gender', 'phone', 'dob', 'age', 'status', 'address','email',
		 'occupation','payment', 'image','patient_identification',)

		def clean_email(self):
			email = self.cleaned_data.get('email')

class AddPatientMedicalForm(forms.ModelForm):
	blood_group= forms.ChoiceField(choices=[('A+', 'A+'),('A-', 'A-'),('B+', 'B+'),('B-', 'B-'),('O+', 'O+'),('O-', 'O-')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))

	weight= forms.CharField(max_length=100,
							widget=forms.TextInput(attrs={'name'	: 	'weight',
														  'class'	:	'form-control',
														  'type'	:	'text',
														  'placeholder':'Patient Weight', }))
	allergies= forms.CharField(max_length=100,
							widget=forms.TextInput(attrs={'name'	: 	'allergies',
														  'class'	:	'form-control',
														  'type'	:	'text',
														  'placeholder':'Patient Allergies', }))
	diabetic 	= 	forms.ChoiceField(choices=[('No', 'No'),('Yes', 'Yes'),('Not Known', 'Not Known')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))

	high_blood_pressure 	= 	forms.CharField(max_length=100,
							widget=forms.TextInput(attrs={'name'	: 	'high_blood_pressure',
														  'class'	:	'form-control',
														  'type'	:	'text',
														  'placeholder':'High blood Pressure', }))

	seizures 	= 	forms.ChoiceField(choices=[('No', 'No'),('Yes', 'Yes'),('Not Known','Not Known')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))

	liver_desease 	= 	forms.ChoiceField(choices=[('No', 'No'),('Yes', 'Yes'),('Not Known', 'Not Known')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))

	ulcers 	= 	forms.ChoiceField(choices=[('No', 'No'),('Yes', 'Yes'),('Not Known','Not Known')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))

	gout 	= 	forms.ChoiceField(choices=[('No', 'No'),('Yes', 'Yes'),('Not Known','Not Known')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))

	heart_desease 	= 	forms.ChoiceField(choices=[('No', 'No'),('Yes', 'Yes'),('Not Known','Not Known')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))

	heart_valve_desease = forms.ChoiceField(choices=[('No', 'No'),('Yes', 'Yes'),('Not Known','Not Known')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))

	lung_desease	=	forms.ChoiceField(choices=[('No', 'No'),('Yes', 'Yes'),('Not Known','Not Known')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))

	cancer			=	forms.CharField(max_length=100,
							widget=forms.TextInput(attrs={'name'	: 	'cancer',
														  'class'	:	'form-control',
														  'type'	:	'text',
														  'placeholder':'If yes precise which cancer', }))

	thyroid_desease	=	forms.ChoiceField(choices=[('No', 'No'),('Yes', 'Yes'),('Not Known','Not Known')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))
	class Meta:
		model	= Patient
		fields	= ('blood_group','weight','allergies','diabetic','high_blood_pressure',
		'seizures','liver_desease','ulcers','gout','heart_desease','heart_valve_desease','lung_desease','cancer','thyroid_desease')


class AddAppointmentForm(forms.ModelForm):

	docZ = {}
	list_doctors = []
	for doc_info in Doctor.objects.all():
		if doc_info.category.name in docZ:
			docZ[doc_info.category.name].append(doc_info.name)
		else:
			docZ[doc_info.category.name] = [doc_info.name]
		list_doctors.append((doc_info.name, doc_info.name))

	priceZ = {}
	list_prices = []
	for price_info in Prices.objects.all():
		if price_info.doctor.name in priceZ:
			priceZ[price_info.doctor.name].append(price_info.amount)
		else:
			priceZ[price_info.doctor.name] = [price_info.amount]
		list_prices.append((price_info.amount, price_info.amount))

	#category = Category.objects.all()
	categories = [str(category) for category in Category.objects.all()]

	category_select = 	forms.ChoiceField(label='Doctor Category', choices=([(category, category) for category in categories]),
							widget=forms.Select(attrs={	'class'		:	'form-control',
														'id'		:	'category',
														'name'		:	'department',
														}))

	doctor_select 	= 	forms.ChoiceField(label='Doctor', choices=(list_doctors),
							widget=forms.Select(attrs={	'class'		:	'form-control',
														'id'		:	'id_doctor',
														'disabled'	:	'true', }))

	price_select 	= 	forms.ChoiceField(label='Price', choices=(list_prices),
							widget=forms.Select(attrs={	'class'		:	'form-control',
														'id'		:	'id_price',
														'disabled'	:	'true', }))

	categories 	= 	json.dumps(categories)
	doctors 	=	json.dumps(docZ)
	prices 		=	json.dumps(priceZ)


	class Meta:
		model = Appointment
		fields = ('category_select', 'doctor_select','price_select')

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
	payment_type = forms.ChoiceField(choices=[('', 'Select Payment method'),('Cash', 'Cash'),('Mobile Money', 'Mobile Money'),('Credit Card', 'Credit Card')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))
	class Meta:
		model 	=	CashAppointmentStatus
		fields	=	['status','payment_type']

class PaymentLabStatusUpdate(forms.ModelForm):
	status = forms.ChoiceField(choices=[('', 'Select Status of the Payment'),('Unpaid', 'Unpaid'),('Paid', 'Paid')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))

	payment_type = forms.ChoiceField(choices=[('', 'Select Payment method'),('Cash', 'Cash'),('Mobile Money', 'Mobile Money'),('Credit Card', 'Credit Card')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))
	class Meta:
		model 	=	CashLabStatus
		fields	=	['status','payment_type']


class MorturyPaymentUpdate(forms.ModelForm):
	status=	forms.ChoiceField(choices=[('', 'Select Status of the Payment'),('Not Paid', 'Not Paid'),('Paid', 'Paid')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))

	class Meta:
		model 	=	Mpayment
		fields	=	['status']

# class PaymentPharmacyStatusUpdate(forms.ModelForm):
# 	status = forms.ChoiceField(choices=[('', 'Select Status of the Payment'),('Unpaid', 'Unpaid'),('Paid', 'Paid')],
# 							widget=forms.Select(attrs={	'class'	:	'form-control', }))
# 	class Meta:
# 		model 	=	CashPharmacyStatus
# 		fields	=	['status']
