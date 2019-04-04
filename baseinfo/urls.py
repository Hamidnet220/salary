from django.urls import path
from .views import *



urlpatterns=[
    path('organization/addnew',AddOrganizationView.as_view(),name="add_organization"),
    path('organizations/',orgnizations_view,name="organizations"),
    path('employeeStatus/addnew',AddEmployeeStatusView.as_view(),name="add_employeeStatus"),
    path('workstatus/addnew',AddWorkStatusView.as_view(),name="add_workstatus"),
    path('maritalstatus/addnew',AddMaritalStatusView.as_view(),name="add_maritalstatus"),
    path('bank/addnew',AddBankView.as_view(),name="add_bank"),
    path('workgroup/addnew',AddWorkGroupView.as_view(),name="add_workgroup"),
    path('workplace/addnew',AddWorkPlaceView.as_view(),name="add_workplace"),
    path('postplace/addnew',AddPostPlaceView.as_view(),name="add_postplace"),
    path('employee/addnew',AddEmployeeView.as_view(),name="add_employee"),

]