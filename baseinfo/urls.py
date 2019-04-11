from django.urls import path
from .views.employee_view import *
from .views.employer_view import *
from .views.general_view import *

urlpatterns=[
    path('organization/addnew',AddOrganizationView.as_view(),name="add_organization"),
    path('organizations/',organization_list_view,name="organizations"),
    path('employeeStatus/addnew',AddEmployeeStatusView.as_view(),name="add_employeeStatus"),
    path('workstatus/addnew',AddWorkStatusView.as_view(),name="add_workstatus"),
    path('maritalstatus/addnew',AddMaritalStatusView.as_view(),name="add_maritalstatus"),
    path('bank/addnew',AddBankView.as_view(),name="add_bank"),
    path('workgroup/addnew',AddWorkGroupView.as_view(),name="add_workgroup"),
    path('workplace/addnew',AddWorkPlaceView.as_view(),name="add_workplace"),
    path('postplace/addnew',AddPostPlaceView.as_view(),name="add_postplace"),
    path('employee/addnew',AddEmployeeView.as_view(),name="add_employee"),

]

urlpatterns+=[
    path('employees/',employees_list_view,name="employees"),
    path('employeestatus/',employee_status_list_view,name="employee_status"),
    path('workstatus/',work_status_list_View,name="work_status"),
    path('maritalstatus/',marital_status_list_view,name="marital_status"),
    path('banks/',bank_list_view,name="banks_list"),
    path('workgroups/',work_group_list_view,name="workgroup_list"),
    path('workplaces/',work_place_list_view,name="workplace_list"),
    path('postplaces/',post_place_list_view,name="postplace_llist"),

]
