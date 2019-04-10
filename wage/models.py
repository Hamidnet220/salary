from django.db import models
from baseinfo.models import *
import datetime
# Create your models here.

class PayType(models.Model):
    title       = models.CharField(max_length=150,verbose_name="عنوان نوع پرداخت")
    description = models.TextField(verbose_name=u"توضیحات")


class AdvanceAndLoan (models.Model):
    employee            = models.ForeignKey(Employee,on_delete=models.PROTECT,verbose_name=u"نام و نام خانوادگی")
    pay_date            = models.DateField(auto_now_add=True,verbose_name=u"تاریخ پرداخت")
    amount              = models.DecimalField(max_digits=11,decimal_places=5,verbose_name=u"مبلغ")
    description         = models.TextField(null=True,blank=True,verbose_name=u"توضیحات")

class Wage(models.Model):
    title       = models.CharField(max_length=150,verbose_name=u"عنوان لیست")
    year        = models.IntegerField(verbose_name=u"سال")
    month       = models.IntegerField(verbose_name=u"ماه")
    pay_type    = models.ForeignKey(PayType,on_delete=models.PROTECT,verbose_name=u"نوع پرداخت")
    is_locked   = models.BooleanField(verbose_name="وضعیت قفل")

class WageDetail(models.Model):
    wage                    = models.ForeignKey(Wage,on_delete=models.PROTECT,verbose_name=u"نام لیست")
    employee                = models.ForeignKey(Employee,on_delete=models.PROTECT,verbose_name=u"نام ونام خانوادگی")
    work_group              = models.ForeignKey(WorkGroup,on_delete=models.PROTECT,verbose_name=u"گروه شغلی")
    daily_base              = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"‍پایه روزانه")
    work_days               = models.SmallIntegerField(verbose_name=u"تعداد روز کارکرد")
    absent_days             = models.SmallIntegerField(verbose_name=u"روز غیبت")
    tiemoff_days            = models.SmallIntegerField(verbose_name=u"روز مرخصی")
    workdays_in_friday      = models.SmallIntegerField(verbose_name=u"جمعه کاری")
    workdays_in_holiday     = models.SmallIntegerField(verbose_name=u"تعطیل کاری")
    work_as_replace         = models.SmallIntegerField(verbose_name=u"جایگزینی")
    workdays_in_mission     = models.SmallIntegerField(verbose_name=u"ماموریت")
    is_shift                = models.BooleanField(default=True,verbose_name=u"وضعیت نوبتکاری")
    ovettime_houre          = models.DecimalField(max_digits=3,decimal_places=3,verbose_name=u"ساعت اضافه کاری")
    children_benefit        = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"حق اولاد")
    monthly_wage_amount     = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"حقوق ماهیانه")
    shift_amount            = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"مبلغ نوبتکاری")
    work_in_holiday_amount  = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"مبلغ تعطیل کاری")
    work_in_friday_amount   = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"مبلغ جمعه کاری")
    work_overtime_amount    = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"مبلغ اضافه کاری")
    work_as_replace_amount  = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"مبلغ جایگزینی")
    commute_amont           = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"مبلغ ایاب و ذهاب")
    bad_wether_right        = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"بدی آب و هوا")
    hygiene_benefit         = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"حق بهداشت")
    food_benefit            = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"حق غذا")
    instruct_amount         = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"مبلغ آموزش")
    backpay_amount          = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"معوق مشمول")
    backpay_tax_exempt      = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"معوق غیر مشمول")
    gross_amount            = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"مبلغ ناخالص")
    tax_include             = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"مشمول مالیات")
    tax_amount              = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"مبلغ مالیات")
    insurance_include       = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"مشمول بیمه")
    insurance_amount        = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"مبلغ بیمه")
    Loan_and_advance        = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"وام و مساعده")
    pay_in_advance          = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"علی الحساب")
    deduction1              = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"سایر کسورات۱")
    deduction2              = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"سایر کسورات ۲")
    net_pay                 = models.DecimalField(max_digits=11,decimal_places=3,verbose_name=u"خالص پرداختی")
    public_message          = models.TextField(verbose_name=u"پیام عمومی")
    private_message         = models.TextField(verbose_name=u"پیام اختصاصی")             
    


