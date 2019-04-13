from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,FormView
from wage.models import *
from wage.forms import *
from views_generator import ViewGenerator

class WageAddView(FormView):
    template_name='input_form.html'
    form_class=AddWageForm
    success_url=reverse_lazy('wages_list')

    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)



def wage_list_view(request,*args,**kwargs):
    view=ViewGenerator(Wage,{'edit_obj':'ویرایش','delete_obj':'حذف','wage_details':'ریز حقوق','attendance_details':'ریز کارکرد'},True,'add_wage')
    return render(request,'list_objects.html',view.get_context_template())

def wage_detail_list_view(request,*args,**kwargs):
    view=ViewGenerator(WageDetail,{},True,'home')
    return render(request,'list_objects.html',view.get_context_template())

class LoanAddView(FormView):
    form_class=AddNewLoanForm
    template_name='input_form.html'
    success_url=reverse_lazy('loans_list')
    
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

def update_loan_viwe(request,id,*args,**kwargs):
    instance=AdvanceAndLoan.objects.get(id=id)
    form=AddNewLoanForm(request.POST or None,instance=instance)
    
    if form.is_valid():
        form.save()
        return redirect('loans_list')
    return render (request,'input_form.html',{'form':form})

def loan_list_view(request,*args,**kwargs):
    view=ViewGenerator(AdvanceAndLoan,{'edit':'ویرایش','delete':'حذف'},False,'add_loan')
    return render(request,'list_objects.html',view.get_context_template())

def paytype_list_view(request,*args,**kwargs):
    view=ViewGenerator(PayType)
    return render(request,'list_objects.html',view.get_context_template())
