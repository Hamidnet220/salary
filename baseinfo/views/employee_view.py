from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from baseinfo.forms import *
from baseinfo.models import *
from views_generator import ViewGenerator


def employees_list_view(request,*args,**kwargs):
    view=ViewGenerator(Employee,{'edit_obj':['ویرایش','edit_employee'],'delete_obj':['حذف','del_employee']},True,'add_employee')
    return render(request,'list_objects.html',view.get_context_template())


class AddEmployeeView(FormView):
    template_name='input_form.html'
    form_class=EmployeeForm
    success_url=reverse_lazy('emplooyees_list')

    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)


def edit_employee_view(request,id,*arg,**kwargs):
    instance=Employee.objects.get(id=id)
    form=EmployeeFormModel(request.POST or None,instance=instance)

    if form.is_valid():
        form.update_record(id)
        return redirect('employees_list')
    return render(request,'input_form.html',{'form':form})
