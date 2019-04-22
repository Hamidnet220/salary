from django import template
from django.conf import settings
register = template.Library()

@register.filter(name='times')
def times(value):
    return range(value)
    
        
   
   
