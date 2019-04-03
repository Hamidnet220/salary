from django import forms
from .models import *

class EmployerForm(forms.Form):
    title           = forms.CharField(max_length=60)
    tel             = forms.CharField(max_length=19)
    fax             = forms.CharField(max_length=19)
    address         = forms.CharField(required=False)
    insurance_code  = forms.CharField(max_length=20)

    def save_record(self):
        Employer.objects.create(**self.cleaned_data)

class EmployeeStatusForm(forms.Form):
    title           = forms.CharField(max_length=50)
    description     = forms.CharField(widget=forms.Textarea)

    def save_record(self):
        EmployeeStatus.objects.create(**self.cleaned_data)
