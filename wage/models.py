from django.db import models
from baseinfo.models import *
import datetime
# Create your models here.

class PayType(models.Model):
    title       = models.CharField(max_length=150)
    description = models.TextField()


class AdvanceAndLoan (models.Model):
    employee            = models.ForeignKey(Employee,on_delete=models.PROTECT)
    pay_date            = models.DateField(auto_now_add=True)
    amount              = models.DecimalField(max_digits=11,decimal_places=5)
    description         = models.TextField(null=True,blank=True)

class Wage(models.Model):
    title       = models.CharField(max_length=150)
    year        = models.IntegerField()
    month       = models.IntegerField()
    pay_type    = models.ForeignKey(PayType,on_delete=models.PROTECT)
    is_locked   = models.BooleanField()

class WageDetail(models.Model):
    wage                = models.ForeignKey(Wage,on_delete=models.PROTECT)
    employee            = models.ForeignKey(Employee,on_delete=models.PROTECT)
    gross_amount        = models.DecimalField(max_digits=11,decimal_places=5)
    tax_amount          = models.DecimalField(max_digits=11,decimal_places=5)
    insurance_amount    = models.DecimalField(max_digits=11,decimal_places=5)
    Loan_and_advance    = models.DecimalField(max_digits=11,decimal_places=5)
    deduction1          = models.DecimalField(max_digits=11,decimal_places=5)
    deduction2          = models.DecimalField(max_digits=11,decimal_places=5)
    net_pay             = models.DecimalField(max_digits=11,decimal_places=5)



