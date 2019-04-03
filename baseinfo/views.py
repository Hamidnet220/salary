from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import *

# Create your views here.
def home_view(request,*args,**kwargs):
    return render(request,"home.html",{})

class add_organization_view(FormView):
    template_name='input_form.html'
    form_class=EmployerForm
    success_url='/home/'
    def form_valid(self, form):
        form.add_record()
        return super().form_valid(form)

