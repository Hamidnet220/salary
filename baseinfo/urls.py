from django.urls import path
from .views.employee_view import *
from .views.employer_view import *
from .views.general_view import *

# employee urls
urlpatterns=[
    path('organization/addnew',AddOrganizationView.as_view(),name="add_employer"),
    path('employeeStatus/addnew',AddEmployeeStatusView.as_view(),name="add_employeestatus"),
    path('workstatus/addnew',AddWorkStatusView.as_view(),name="add_workstatus"),
    path('maritalstatus/addnew',AddMaritalStatusView.as_view(),name="add_maritalstatus"),
    path('bank/addnew',AddBankView.as_view(),name="add_bank"),
    path('workgroup/addnew',AddWorkGroupView.as_view(),name="add_workgroup"),
    path('workplace/addnew',AddWorkPlaceView.as_view(),name="add_workplace"),
    path('postplace/addnew',AddPostPlaceView.as_view(),name="add_postplace"),
    path('addemployee/',AddEmployeeView.as_view(),name="add_employee"),
    path('militaryservstatus/',military_status_list_view,name="militaryservs_list"),
    path('addmilitarystat/',AddMilitaryStatus.as_view(),name='add_militaryservstat'),
    path('editmilitarystat/<int:id>',AddMilitaryStatus.as_view(),name='edit_militaryservstat'),
    path('delmilitarystat/<int:id>',AddMilitaryStatus.as_view(),name='del_militaryservstat'),
    path('cities/',citiy_list_view,name="cities_list"),
    path('addcity/',AddCityView.as_view(),name="add_city"),
    path('countries/',country_list_view,name="countries_list"),
    path('addcountry/',AddCountryView.as_view(),name="add_country"),


]

# employer urls

urlpatterns+=[
    path('employers/',organization_list_view,name="employers_list"),
    path('editemployer/<int:id>',edit_employer_view,name="edit_employer"),
    path('delemployer/<int:id>',delete_employer_view,name="del_employer"),
    path('employees/',employees_list_view,name="employees_list"),
    path('employeestatus/',employee_status_list_view,name="employeestatuses_list"),
    path('workstatus/',work_status_list_View,name="workstatuses_list"),
    path('editworkstatus/<int:id>',edit_work_status_view,name="edit_workstatus"),
    path('delworkstatus/<int:id>',edit_work_status_view,name="del_workstatus"),
    path('maritalstatus/',marital_status_list_view,name="maritalstatuses_list"),
    path('banks/',bank_list_view,name="banks_list"),
    path('workgroups/',work_group_list_view,name="workgroups_list"),
    path('workplaces/',work_place_list_view,name="workplaces_list"),
    path('postplaces/',post_place_list_view,name="postplaces_llist"),

]

urlpatterns+=[
    path('editemployee/<int:id>',edit_employee_view,name="edit_employee"),

]

urlpatterns+=[
    path('delemployee/<int:id>',AddEmployeeView.as_view(),name="del_employee"),
    path('delworkstatus/',work_status_list_View,name="del_workstatus"),


]

