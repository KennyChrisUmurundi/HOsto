from django import forms
from .models import Drugs,TakenDrugs,Category,DrugsSupplier


class AddDrugsForm(forms.ModelForm):
    name                  =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text'}))
    category              = forms.ModelChoiceField(queryset=Category.objects.all(),
							widget=forms.Select(attrs={	'class'		:	'form-control', }))
    pricePerUnit          =   forms.IntegerField(widget=forms.TextInput(attrs={'name':'name','class':'form-control number','type':'number','min':'0','onkeypress':'return isNumberKey(event)'}))
    quantity                 =   forms.IntegerField(widget=forms.TextInput(attrs={'name':'name','class':'form-control number','type':'number','min':'0','onkeypress':'return isNumberKey(event)'}))
    purchasedPrice        =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control number','type':'number','min':'0','onkeypress':'return isNumberKey(event)'}))
    supplier              =   forms.ModelChoiceField(queryset=DrugsSupplier.objects.all(),
							widget=forms.Select(attrs={	'class'		:	'form-control', }))
    effects               =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text'}))
    expire_date	       	  =	  forms.CharField(max_length=300,
							widget=forms.TextInput(attrs={'name'	: 	'dob',
														  'class'	:	'form-control',
														  'type'	:	'date',
														  }))


    class Meta:
        model   =   Drugs
        fields  =('name','category','pricePerUnit','quantity','purchasedPrice','supplier','effects','expire_date',)


class AddTakenDrugsForm(forms.ModelForm):
    quantity    =   forms.IntegerField(widget=forms.TextInput(attrs={'name':'name','class':'form-control number','type':'number','min':'1','onkeypress':'return isNumberKey(event)'}))




    class Meta:
        model    =  TakenDrugs
        fields   =  ('quantity',)


class AddDrugsCForm(forms.ModelForm):
    category    =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text'}))

    description      =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text'}))



    class Meta:
        model    =  Category
        fields   =  ('category','description',)

class AddDrugsSupplierForm(forms.ModelForm):
    name    =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text'}))

    address      =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text'}))

    phone      =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text'}))

    email      =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text'}))



    class Meta:
        model    =  DrugsSupplier
        fields   =  ('name','address','phone','email',)

class LoadOutofStock(forms.ModelForm):

    quantity       =     forms.IntegerField(widget=forms.TextInput(attrs={'name':'name','class':'form-control number','type':'number','min':'1','onkeypress':'return isNumberKey(event)'}))
    supplier              =   forms.ModelChoiceField(queryset=DrugsSupplier.objects.all(),
							widget=forms.Select(attrs={	'class'		:	'form-control', }))

    expire_date	       	  =	  forms.CharField(max_length=300,
							widget=forms.TextInput(attrs={'name'	: 	'dob',
														  'class'	:	'form-control',
														  'type'	:	'date',
														  }))

    class Meta:
        model   =   Drugs
        fields  =   ('quantity','supplier','expire_date',)
