from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from baseinfo.forms import *
from baseinfo.models import *
from views_generator import ViewGenerator


def employees_list_view(request,*args,**kwargs):
    view=ViewGenerator(Employee,True,True,'add_employee')
    return render(request,'list_objects.html',view.get_context_template())


class AddEmployeeView(FormView):
    template_name='input_form.html'
    form_class=EmployeeForm
    success_url='/success/'

    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)
