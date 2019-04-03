from django.urls import path
from .views import *



urlpatterns=[
    path('organization/addnew',add_organization_view.as_view(),name="add_organization")
]