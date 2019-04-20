from django.db import models
from wage.models import Wage
from baseinfo.models import Employee
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class ShiftName(models.Model):
    code         = models.IntegerField(unique=True)
    title        = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=10   )
    description  = models.TextField(blank=True,null=True)

    def __str__(self):
        return "{},{}".format(self.title,self.code)


class Worksheet(models.Model):
    wage            = models.ForeignKey(Wage,on_delete=models.PROTECT)
    employee        = models.ForeignKey(Employee,on_delete=models.PROTECT)
    work_days_stat   = ArrayField(models.IntegerField(blank=True,null=True),size=31,)

    def __str__(self):
        return "{}-{}-{}".format(self.wage,self.work_days_stat,self.employee)
    

