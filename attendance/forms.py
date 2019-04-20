from django import forms
from .models import *
import datetime


class AddWorksheet(forms.Form):
    pass
#     wage        =   forms.ModelChoiceField(Wage.objects.all(),label="لیست حقوق:")
#     employee    =   forms.ModelChoiceField(Employee.objects.all(),label='نام و نام خانوادگی:')
#     day1          =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='01')
#     day2          =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='02')
#     day3          =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='03')
#     day4          =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='04')
#     day5          =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='05')
#     day6          =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='06')
#     day7          =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='07')
#     day8          =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='08')
#     day9          =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='09')
#     day10         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='10')
#     day11         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='11')
#     day12         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='12')
#     day13         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='13')
#     day14         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='14')
#     day15         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='15')
#     day16         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='16')
#     day17         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='17')
#     day18         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='18')
#     day19         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='19')
#     day20         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='20')
#     day21         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='21')
#     day22         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='22')
#     day23         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='23')
#     day24         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='24')
#     day25         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='25')
#     day26         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='26')
#     day27         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='27')
#     day28         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='28')
#     day29         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='29')
#     day30         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='30')
#     day31         =   forms.ModelChoiceField(WorkdayStaus.objects.all(),label='31')

#     def save_record(self):
#         days=list()
#         for key,value in self.cleaned_data.items():
#             if 'day' in key:
#                 days.append(self.cleaned_data[key])

#         date = datetime.date.today()
        
#         for day in days:
#             self.cleaned_data.update({'date':date,'work_day_stat':days[0]})
#             obj=dict()
#             obj.update({'date':date,'work_day_stat':day,'employee':self.cleaned_data['employee'],'wage':self.cleaned_data['wage']})
#             print(obj)
#             Worksheet.objects.create(**obj)
#             date+=datetime.timedelta(1)
        