from django import template
from django.conf import settings
import re
from attendance.models import *
from khayyam import *
import datetime 
import math
register = template.Library()

@register.filter
def getrows(value):
    wage=Wage.objects.get(id=value)
    start_date=JalaliDate(wage.year,wage.month)
    days_of_month=start_date.daysinmonth
    end_date=start_date+datetime.timedelta(days_of_month-1)
    rownumber=math.ceil(days_of_month/7)

    """Gets an attribute of an object dynamically from a string name"""
    return rownumber
    
        
   
   
