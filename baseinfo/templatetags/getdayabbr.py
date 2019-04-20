from django import template
from django.conf import settings
import re
from attendance.models import *

numeric_test = re.compile("^\d+$")
register = template.Library()

@register.filter(name='getdayabbr')
def getdayabbr(value):
    """Gets an attribute of an object dynamically from a string name"""
    try:
        day_filter=ShiftName.objects.get(code=value)
        day_abbr=getattr(day_filter,'abbreviation')
        return day_abbr
    except:
         return '-'
    
        
   
   
