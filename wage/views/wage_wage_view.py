from django.shortcuts import render
from django.views.generic import TemplateView
from wage.models import *
from views_generator import ViewGenerator


def wage_list_view(request,*args,**kwargs):
    view=ViewGenerator(Wage,'home')
    return render(request,'list_objects.html',view.get_context_template())

def wage_detail_list_view(request,*args,**kwargs):
    view=ViewGenerator(WageDetail)
    return render(request,'list_objects.html',view.get_context_template())

def loan_list_view(request,*args,**kwargs):
    view=ViewGenerator(AdvanceAndLoan)
    return render(request,'list_objects.html',view.get_context_template())

def paytype_list_view(request,*args,**kwargs):
    view=ViewGenerator(PayType)
    return render(request,'list_objects.html',view.get_context_template())
