from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from baseinfo.forms import *
from baseinfo.models import *


def employees_list_view(request,*args,**kwargs):
    context={
    'objects':Employee.objects.filter(),
    'titles':['نام','نام خانوادگی','نام پدر','کد ملی','شماره شناسنامه',
            'کد بیمه','وضعیت','محل کار','محل پست','وضعیت تاهل',
            'تعداد فرزند','گروه شغلی','معاف از مالیات','معاف از بیمه','تلفن','موبایل','توضیحات'],
    'field_names':['firstname','lastname','fathername','national_code',
                    'id_number','insurance_id','employee_status','work_place',
                    'post_place','marital_status','children_count',
                    'work_group','tax_exempt','indsurence_exempt','tel','mobile','description'],
    'add_url_name':'add_employee',
    }
    return render(request,'list_objects.html',context)


class AddEmployeeView(FormView):
    template_name='input_form.html'
    form_class=EmployeeForm
    success_url='/success/'

    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)
