from django.urls import path
from .views import *
urlpatterns=[
    path('worksheet/',LogsheetView.as_view(),name="loghsheet"),
]