from django import forms
from django.forms import ModelForm
from .models import icuFindings



class AddFeedbackForm(forms.ModelForm):
    findings        =   forms.CharField(max_length=200,widget=forms.TextInput(attrs={'name':'name','class':'form-control','type':'text','style':'height:100px;width:40%'}))



    class Meta:
        model   =   icuFindings
        fields  =('findings',)
