from django import forms
from django.forms import ModelForm
from .models import Results,TestStatus



class AddResultsForm(forms.ModelForm):
    findings        =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text','style':'height:100px;width:40%'}))


    class Meta:
        model   =   Results
        fields  =('findings',)

class AddTeststatusForm(forms.ModelForm):
    status = forms.ChoiceField(choices=[('', 'Status of test'),('Done', 'Done'),('Not Done', 'Not Done')],
							widget=forms.Select(attrs={	'class'	:	'form-control', }))

    class Meta:
        model  = TestStatus
        fields  =('status',)
