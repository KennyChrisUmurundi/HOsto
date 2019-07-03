from django import forms
from .models import Drugs,TakenDrugs


class AddDrugsForm(forms.ModelForm):
    name        =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text','placeholder':'Enter Drug name'}))
    category        =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text','placeholder':'Enter Drug category'}))
    pricePerUnit        =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text','placeholder':'Enter Drug pricePerUnit'}))


    class Meta:
        model   =   Drugs
        fields  =('name','category','pricePerUnit',)


class AddTakenDrugsForm(forms.ModelForm):
    quantity    =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'quantity','class':'form-control','type':'text','placeholder':'Enter quantity'}))

    status      =   forms.ChoiceField(choices=[('Paid', 'Paid'),('Not Paid', 'Not Paid')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))



    class Meta:
        model    =  TakenDrugs
        fields   =  ('quantity','status',)
