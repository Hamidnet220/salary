from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from baseinfo.forms import *
from baseinfo.models import *



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

class AddOrganizationView(FormView):
    template_name='input_form.html'
    form_class=EmployerForm
    success_url='/organizations/'
    
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)
