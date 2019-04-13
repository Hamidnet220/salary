from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from baseinfo.forms import *
from baseinfo.models import *



def orgnizations_view(request,*args,**kwargs):
    render(request,'organizations.html',{})


def organization_list_view(request,*args,**kwargs):
    view=ViewGenerator(Employer,{'edit_obj':'ویرایش','delete_obj':'حذف'},True,'add_employer')
    return render(request,'list_objects.html',view.get_context_template())

class AddOrganizationView(FormView):
    template_name='input_form.html'
    form_class=EmployerForm
    success_url=reverse_lazy('employers_list ')
    
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)
