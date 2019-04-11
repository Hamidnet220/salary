from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from baseinfo.forms import *
from baseinfo.models import *
from views_generator import ViewGenerator

# Create your views here.
class home_view(TemplateView):
    template_name='home.html'

class AddEmployeeStatusView(FormView):
    template_name='input_form.html'
    form_class=EmployeeStatusForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)
        
def employee_status_list_view(request,*args,**kwargs):
    view=ViewGenerator(EmployeeStatus,'add_employeestatus')
    return render(request,"list_objects.html",view.get_context_template())

class AddWorkStatusView(FormView):
    template_name='input_form.html'
    form_class=WorkStatusForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

def work_status_list_View(request,*args,**kwargs):
    view=ViewGenerator(WorkStatus,'add_workstatus')
    return render(request,"list_objects.html",view.get_context_template())

class AddMaritalStatusView(FormView):
    template_name='input_form.html'
    form_class=MaritalStatusForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

def marital_status_list_view(request,*args,**kwargs):
    view=ViewGenerator(MaritalStatus,'add_maritalstatus')
    return render(request,"list_objects.html",view.get_context_template())
        
class AddBankView(FormView):
    template_name='input_form.html'
    form_class=BankForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

def bank_list_view(request,*args,**kwargs):
    view=ViewGenerator(Bank,'add_bank')
    return render(request,"list_objects.html",view.get_context_template())

class AddWorkGroupView(FormView):
    template_name='input_form.html'
    form_class=WorkGroupForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

def work_group_list_view(request,*args,**kwargs):
    view=ViewGenerator(WorkGroup,'add_workgroup')
    return render(request,"list_objects.html",view.get_context_template())

class AddWorkPlaceView(FormView):
    template_name='input_form.html'
    form_class=WorkPlaceForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

def work_place_list_view(request,*args,**kwargs):
    view=ViewGenerator(WorkPlace,'add_workplace')
    return render(request,"list_objects.html",view.get_context_template())

class AddPostPlaceView(FormView):
    template_name='input_form.html'
    form_class=PostPlaceForm
    success_url='/success/'
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

def post_place_list_view(request,*args,**kwargs):
    view=ViewGenerator(PostPlace,'add_postplace')
    return render(request,"list_objects.html",view.get_context_template())


