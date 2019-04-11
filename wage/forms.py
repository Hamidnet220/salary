from django import forms
from .models import *

class AddWageForm(forms.ModelForm):
    class Meta:
        model=Wage
        fields='__all__'
    def save_record(self):
        Wage.objects.create(**self.cleaned_data)

class AddNewLoanForm(forms.ModelForm):
    
    class Meta:

        model=AdvanceAndLoan
        fields= '__all__'

    
    def save_record(self):
        AdvanceAndLoan.objects.create(**self.cleaned_data)


