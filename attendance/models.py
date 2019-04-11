from django.db import models
from wage.models import Wage
from baseinfo.models import Employee
# Create your models here.

class WorkdayStaus(models.Model):
    title       = models.CharField(max_length=20)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.title


class Worksheet(models.Model):
    wage            = models.ForeignKey(Wage,on_delete=models.PROTECT)
    employee        = models.ForeignKey(Employee,on_delete=models.PROTECT)
    date            = models.DateField()
    work_day_stat   = models.ForeignKey(WorkdayStaus,on_delete=models.PROTECT)
    

