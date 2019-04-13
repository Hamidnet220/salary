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
    title           = forms.CharField(label="عنوان وضعیت کارکنان:",max_length=50)
    description     = forms.CharField(label="توضیحات:",widget=forms.Textarea)

    def save_record(self):
        EmployeeStatus.objects.create(**self.cleaned_data)

class WorkStatusForm(forms.Form):
    title           = forms.CharField(label="عنوان وضعیت کاری:",max_length=50)
    description     = forms.CharField(label="توضیحات:",widget=forms.Textarea,required=False)

    def save_record(self):
        WorkStatus.objects.create(**self.cleaned_data)

class MaritalStatusForm(forms.Form):
    title           = forms.CharField(label="عنوان وضعیت تاهل:",max_length=20)
    description     = forms.CharField(label="توضیحات:",widget=forms.Textarea,required=False)

    def save_record(self):
        MaritalStatus.objects.create(**self.cleaned_data)

class BankForm(forms.Form):
    title           = forms.CharField(label="نام بانک:",max_length=50)
    description     = forms.CharField(label="توضیحات:",required=False,widget=forms.Textarea)

    def save_record(self):
        Bank.objects.create(**self.cleaned_data)

class WorkGroupForm(forms.Form):
    title           = forms.CharField(label="عنوان گروه شغلی:",max_length=100)
    child_benefit   = forms.DecimalField(label="مبلغ حق اولاد برای یک نفر:",max_digits=50,decimal_places=2)
    dwelling_benefit= forms.DecimalField(label="مبلغ حق مسکن:",max_digits=50,decimal_places=2)
    Bon_benefit     = forms.DecimalField(label="مبلغ بن:",max_digits=50,decimal_places=2)

    def save_record(self):
        WorkGroup.objects.create(**self.cleaned_data)

class WorkPlaceForm(forms.Form):
    title           = forms.CharField(label="عنوان محل کار:",max_length=60)
    description     = forms.CharField(label="توضیحات:",required=False,widget=forms.Textarea)

    def save_record(self):
        WorkPlace.objects.create(**self.cleaned_data)


class PostPlaceForm(forms.Form):
    title           = forms.CharField(label="عنوان محل پست:",max_length=60)
    number_of_employee = forms.IntegerField(label="تعداد نفرات پست")
    post_status     = forms.IntegerField(label="وضعیت پست")
    decription      = forms.CharField(label="توضیحات:",required=False,widget=forms.Textarea)
    def save_record(self):
        PostPlace.objects.create(**self.cleaned_data)

class EmployeeForm(forms.Form):
    employer        = forms.ModelChoiceField(Employer.objects.all(),label="نام کارفرما:")
    firstname       = forms.CharField(label="نام:",max_length=50)
    lastname        = forms.CharField(label="نام خانوادگی:",max_length=50)
    fathername      = forms.CharField(label="نام پدر:",max_length=50)
    national_code   = forms.CharField(label="شماره ملی:",max_length=10)
    id_number       = forms.CharField(label="شماره شناسنامه:",max_length=10)
    insurance_id    = forms.CharField(label="کد بیمه:",max_length=10)
    employee_status = forms.ModelChoiceField(EmployeeStatus.objects.all(),label="وضعیت پرسنل:")
    work_place      = forms.ModelChoiceField(WorkPlace.objects.all(),label="محل کار:")
    post_place      = forms.ModelChoiceField(PostPlace.objects.all(),label="محل پست:")
    work_status     = forms.ModelChoiceField(WorkStatus.objects.all(),label="وضعیت شغلی:")
    marital_status  = forms.ModelChoiceField(MaritalStatus.objects.all(),label="وضعیت تاهل:")
    children_count  = forms.IntegerField(label="تعداد فرزند")
    work_group      = forms.ModelChoiceField(WorkGroup.objects.all(),label="گروه شغلی:")
    tax_exempt      = forms.BooleanField(label="معافیت از پرداخت مالیات:")
    indsurence_exempt= forms.BooleanField(label="معافیت از پرداخت بیمه:")
    tel             = forms.CharField(label="تلفن تماس:",max_length=19,required=False)
    mobile          = forms.CharField(label="شماره همراه:",max_length=19,required=False)
    description     = forms.CharField(label="توضسحات:",required=False,widget=forms.Textarea)
    def save_record(self):
        Employee.objects.create(**self.cleaned_data)