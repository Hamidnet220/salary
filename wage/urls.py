from django.urls import path
from .views.wage_wage_view import *
urlpatterns=[
    path('wages/',wage_list_view,name='wage_list'),
    path('wagedetails/',wage_detail_list_view,name='wage_details'),
    path('loanlist/',loan_list_view,name='loan_list'),

]