from django.urls import path
from .views.wage_wage_view import *
urlpatterns=[
    path('wages/',wage_list_view,name='wages_list'),
    path('wagedetails/',wage_detail_list_view,name='wagedetails_list'),
    path('loanlist/',loan_list_view,name='loans_list'),

]

urlpatterns+=[
    path('wage/addnew',WageAddView.as_view(),name='add_wage'),
    path('loan/addnew/',LoanAddView.as_view(),name='add_loan'),

]

urlpatterns+=[
    path('wage/update/<int:id>',update_loan_viwe,name='update_wage')
]