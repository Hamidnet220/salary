from django.urls import path
from .views import *



urlpatterns=[
    path('organization/addnew',AddOrganizationView.as_view(),name="add_organization"),
    path('employeeStatus/addnew',AddEmployeeStatusView.as_view(),name="add_EmployeeStatus"),
]