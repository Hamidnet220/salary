from django import forms
from .models import *

class EmployerForm(forms.Form):
    title           = forms.CharField(max_length=60)
    tel             = forms.CharField(max_length=19)
    fax             = forms.CharField(max_length=19)
    address         = forms.CharField()
    insurance_code  = forms.CharField(max_length=20)

    def add_record(self):
        Employer.objects.create(**self.cleaned_data)
