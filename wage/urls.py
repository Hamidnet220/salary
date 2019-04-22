from django.urls import path
from .views.wage_wage_view import *
urlpatterns=[
    path('wages/',wage_list_view,name='wages_list'),
    path('wagedetails/<int:id>',wage_detail_list_view,name='wagedetails_list'),
    path('loanlist/',loan_list_view,name='loans_list'),
    path('attendancedetails/<int:id>',attendance_detail_list_view,name='attendance_details'),
    path('calculateworksheet/<int:id>',logsheet_detail_view,name='calculate_worksheet'),
    path('importemployees/<int:id>',import_emoloyee_view,name='import_employees'),

    

]

# add urls
urlpatterns+=[
    path('wage/addnew',WageAddView.as_view(),name='add_wage'),
    path('loan/addnew/',LoanAddView.as_view(),name='add_loan'),

]

# edit urls
urlpatterns+=[
    path('wage/update/<int:id>',update_loan_viwe,name='update_wage'),
    path('editwage/<int:id>',LoanAddView.as_view(),name='edit_wage'),

]

# delete urls
urlpatterns+=[
    path('delwage/<int:id>',delete_wage_view,name='del_wage'),

]