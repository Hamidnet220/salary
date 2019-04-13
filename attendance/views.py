from django.shortcuts import render
import datetime
from .models import *
from django.views.generic import TemplateView,FormView
from .forms import *
# Create your views here.

def logsheet_view(request,*args,**kwargs):
    start_date=datetime.date.today()
    end_date=datetime.timedelta(30)
    obj=Worksheet.objects.all()
    
class LogsheetView(FormView):
    form_class=AddWorksheet
    template_name='logsheet.html'
    success_url='/tanks/'
    
    def form_valid(self, form):
        form.save_record()
        return super().form_valid(form)

