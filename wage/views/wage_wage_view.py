from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView,FormView
from wage.models import *
from wage.forms import *
from attendance.models import *
from views_generator import ViewGenerator

class WageAddView(FormView):
    template_name='input_form.html'
    form_class=AddWageForm
    success_url=reverse_lazy('wages_list')

    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

def wage_list_view(request,*args,**kwargs):
    view=ViewGenerator(Wage,
    {'edit_obj':['ویرایش','edit_wage'],'delete_obj':['حذف','del_wage'],
    'wage_details':['ریز حقوق','wagedetails_list'],
    'attendance_details':['ریز کارکرد','attendance_details']}
    ,True,'add_wage')
    return render(request,'list_objects.html',view.get_context_template())

def wage_detail_list_view(request,id,*args,**kwargs):
    wage_detaisl_objs=WageDetail.objects.filter(wage_id=id)
    if wage_detaisl_objs.count()!=0:
        view=ViewGenerator(WageDetail,{},True,'home')
        return render(request,'list_objects.html',view.get_context_template(id))
    context={
        'message':'برای این لیست حقوق ریز حقوق  وجود ندارد آیا می خواهید ایجاد کنید؟',
        'buttons':{'yes':['بله','home'],'no':['خیر','wages_list'],'back':['برگشت به صفحه قبل','wages_list']}
        
    }
    return render(request,'confirm_template.html',context)

def attendance_detail_list_view(request,id,*args,**kwargs):
    wage_detaisl_objs=Worksheet.objects.filter(wage_id=id)
    if wage_detaisl_objs.count()!=0:
        view=ViewGenerator(Worksheet,{},True,'home')
        return render(request,'list_objects.html',view.get_context_template(id))
    context={
        'message':'برای این لیست حقوق ریز کارکرد وجود ندارد آیا می خواهید ایجاد کنید؟',
        'buttons':{'yes':['بله','home'],'no':['خیر','wages_list'],'back':['برگشت به صفحه قبل','wages_list']}
        
    }
    return render(request,'confirm_template.html',context)


class LoanAddView(FormView):
    form_class=AddNewLoanForm
    template_name='input_form.html'
    success_url=reverse_lazy('loans_list')
    
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

def wage_edit_view(request,id,*args,**kwargs):
    instance=Wage.objects.get(id=id)
    form=AddWageForm(request.POST or None,instance=instance)
    if form.is_valid():
        form.save()
        return redirect('wages_list')
    return render(request,'input_form.html',{'form':form})

def delete_wage_view(request,id,*args,**kwargs):
    obj=Wage.objects.get(id=id)
    try:
        obj.delete()
        return redirect('wages_list')
    except Exception as err:
         return HttpResponse('<h1>این لیست دارای ریز حقوق می باشد و شما نمی توانید آن را حذف کنید<h1>')
     
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
