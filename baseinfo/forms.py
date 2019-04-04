from django import forms
from .models import *

class EmployerForm(forms.Form):
    title           = forms.CharField(label="عنوان شرکت/سازمان:",max_length=60)
    tel             = forms.CharField(label="تلفن تماس:",max_length=19)
    fax             = forms.CharField(label="فکس:",max_length=19)
    address         = forms.CharField(label="آدرس:",required=False)
    insurance_code  = forms.CharField(label="کد بیمه:",max_length=20)

    def save_record(self):
        Employer.objects.create(**self.cleaned_data)

class EmployeeStatusForm(forms.Form):
    title           = forms.CharField(label="عنوان وضعیت کاری:",max_length=50)
    description     = forms.CharField(label="توضیحات:",widget=forms.Textarea)

    def save_record(self):
        EmployeeStatus.objects.create(**self.cleaned_data)

class WorkStatusForm(forms.Form):
    title           = forms.CharField(max_length=50)
    description     = forms.CharField(widget=forms.Textarea,required=False)

    def save_record(self):
        WorkStatus.objects.create(**self.cleaned_data)
