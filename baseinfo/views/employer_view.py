from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from baseinfo.forms import *
from baseinfo.models import *



def orgnizations_view(request,*args,**kwargs):
    render(request,'organizations.html',{})


def organization_list_view(request,*args,**kwargs):
    view=ViewGenerator(Employer,{'edit_obj':['ویرایش','edit_employer'],'delete_obj':['حذف','del_employer']},True,'add_employer')
    return render(request,'list_objects.html',view.get_context_template())

def delete_employer_view(request,id,*args,**kwargs):
    obj=Employer.objects.get(id=id)

    try:
        obj.delete()
        return redirect('employers_list')
    except Exception as err:
        print(err.args)
        print(err)
        context={
            'message':'این شرکت اطلاعات دارای مرتبط می باشد لطفا قبل از حذف آن اطلاعات موجود را بررسی کنید.',
            'buttons':{'back':['صفحه قبل','employers_list'],'home':['صفحه اصلی','home'],}
        }
        return render(request,'confirm_template.html',context)


class AddOrganizationView(FormView):
    template_name='input_form.html'
    form_class=EmployerForm
    success_url=reverse_lazy('employers_list')
    
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)
