from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import *
from .models import *

# Create your views here.
class home_view(TemplateView):
    template_name='home.html'

def orgnizations_view(request,*args,**kwargs):
    render(request,'organizations.html',{})

def organization_list_view(request,*args,**kwargs):
    context={
    'objects':Employer.objects.filter(is_deleted=False),
    'titles':['عنوان','تلفن','فکس','آدرس','کد کارگاهی'],
    'field_names':['title','tel','fax','address','insurance_code'],
    'add_url_name':'add_organization',
    }
    return render(request,'list_objects.html',context)

def employees_list_view(request,*args,**kwargs):
    
    context={
    'objects':Employee.objects.filter(),
    'titles':['نام','نام خانوادگی','نام پدر','کد ملی','شماره شناسنامه','کد بیمه','وضعیت','محل کار','محل پست'],
    'field_names':['firstname','lastname','fathername','national_code','id_number','insurance_id',
                    'employee_status','work_place','post_place'],
    'add_url_name':'add_employee',
    }
    return render(request,'list_objects.html',context)
class AddOrganizationView(FormView):
    template_name='input_form.html'
    form_class=EmployerForm
    success_url='/organizations/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

class AddEmployeeStatusView(FormView):
    template_name='input_form.html'
    form_class=EmployeeStatusForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

class AddWorkStatusView(FormView):
    template_name='input_form.html'
    form_class=WorkStatusForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

class AddMaritalStatusView(FormView):
    template_name='input_form.html'
    form_class=MaritalStatusForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)
        
class AddBankView(FormView):
    template_name='input_form.html'
    form_class=BankForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

class AddWorkGroupView(FormView):
    template_name='input_form.html'
    form_class=WorkGroupForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

class AddWorkPlaceView(FormView):
    template_name='input_form.html'
    form_class=WorkPlaceForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

class AddPostPlaceView(FormView):
    template_name='input_form.html'
    form_class=PostPlaceForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

class AddEmployeeView(FormView):
    template_name='input_form.html'
    form_class=EmployeeForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)