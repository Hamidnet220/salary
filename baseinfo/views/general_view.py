from django.shortcuts import render
from django.urls import reverse_lazy
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
    success_url=reverse_lazy('employeestatuses_list')
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)
        
def employee_status_list_view(request,*args,**kwargs):
    view=ViewGenerator(EmployeeStatus,{},False,'add_employeestatus')
    return render(request,"list_objects.html",view.get_context_template())

class AddWorkStatusView(FormView):
    template_name='input_form.html'
    form_class=WorkStatusForm
    success_url=reverse_lazy('workstatuses_list')
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

def work_status_list_View(request,*args,**kwargs):
    view=ViewGenerator(WorkStatus,{},False,'add_workstatus')
    return render(request,"list_objects.html",view.get_context_template())

class AddMaritalStatusView(FormView):
    template_name='input_form.html'
    form_class=MaritalStatusForm
    success_url=reverse_lazy('maritalstatuses_list')
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

def marital_status_list_view(request,*args,**kwargs):
    view=ViewGenerator(MaritalStatus,{},False,'add_maritalstatus')
    return render(request,"list_objects.html",view.get_context_template())
        
class AddBankView(FormView):
    template_name='input_form.html'
    form_class=BankForm
    success_url=reverse_lazy('banks_list')
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

def bank_list_view(request,*args,**kwargs):
    view=ViewGenerator(Bank,{},False,'add_bank')
    return render(request,"list_objects.html",view.get_context_template())

class AddWorkGroupView(FormView):
    template_name='input_form.html'
    form_class=WorkGroupForm
    success_url=reverse_lazy('workgroups_list')
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

def work_group_list_view(request,*args,**kwargs):
    view=ViewGenerator(WorkGroup,{},False,'add_workgroup')
    return render(request,"list_objects.html",view.get_context_template())

class AddWorkPlaceView(FormView):
    template_name='input_form.html'
    form_class=WorkPlaceForm
    success_url=reverse_lazy('workplaces_list')
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

def work_place_list_view(request,*args,**kwargs):
    view=ViewGenerator(WorkPlace,{},False,'add_workplace')
    return render(request,"list_objects.html",view.get_context_template())

class AddPostPlaceView(FormView):
    template_name='input_form.html'
    form_class=PostPlaceForm
    success_url=reverse_lazy('postplaces_list')
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

def post_place_list_view(request,*args,**kwargs):
    view=ViewGenerator(PostPlace,{},False,'add_postplace')
    return render(request,"list_objects.html",view.get_context_template())


