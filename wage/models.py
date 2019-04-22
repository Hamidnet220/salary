from django.db import models
from baseinfo.models import *
import datetime
# Create your models here.

class PayType(models.Model):
    title       = models.CharField(max_length=150,verbose_name="عنوان نوع پرداخت")
    description = models.TextField(verbose_name=u"توضیحات")

    def __str__(self):
        return self.title


class AdvanceAndLoan (models.Model):
    employee            = models.ForeignKey(Employee,on_delete=models.PROTECT,verbose_name=u"نام و نام خانوادگی")
    pay_date            = models.DateField(verbose_name=u"تاریخ پرداخت")
    amount              = models.DecimalField(max_digits=11,decimal_places=5,verbose_name=u"مبلغ")
    description         = models.TextField(null=True,blank=True,verbose_name=u"توضیحات")

    def __str__(self):
        return "{}-{}-{}".format(self.employee,self.pay_date,self.amount)

class Wage(models.Model):
    title                     = models.CharField(max_length=150,verbose_name=u"عنوان لیست")
    year                      = models.IntegerField(verbose_name=u"سال")
    company                   = models.ForeignKey(Employer,on_delete=models.PROTECT,verbose_name=u"شرکت")
    month                     = models.IntegerField(verbose_name=u"ماه")
    total_employees           = models.IntegerField(verbose_name=u"تعداد کارکنان")
    total_workdays            = models.IntegerField(verbose_name=u"تعداد روزهای کاری")
    total_dayoffs             = models.IntegerField(verbose_name=u"جمع روزهای مرخصی")
    total_absents             = models.IntegerField(verbose_name=u"جمع روزهای غیبت")
    total_overtime            = models.IntegerField(verbose_name=u"جمع ساعت اضافه کاری")
    total_gross_amount        = models.DecimalField(max_digits=50,decimal_places=2,verbose_name=u"جمع ناخالص")
    total_insuracne_amount    = models.DecimalField(max_digits=50,decimal_places=2,verbose_name=u"مبلغ بیمه")
    total_7per_insur_amount   = models.DecimalField(max_digits=50,decimal_places=2,verbose_name=u"مبلغ ۷٪ بیمه")
    total_23per_insur_amount  = models.DecimalField(max_digits=50,decimal_places=2,verbose_name=u"مبلغ 23٪ بیمه")
    total_tax_included_amount = models.DecimalField(max_digits=50,decimal_places=2,verbose_name=u"مبلغ مشمول مالیات")
    total_tax_amount          = models.DecimalField(max_digits=50,decimal_places=2,verbose_name=u"جمع مالیات")
    total_net_amount          = models.DecimalField(max_digits=50,decimal_places=2,verbose_name=u"جمع خالص پرداختی")
    pay_type                  = models.ForeignKey(PayType,on_delete=models.PROTECT,verbose_name=u"نوع پرداخت")
    is_locked                 = models.BooleanField(verbose_name="وضعیت قفل")

    def __str__(self):
        return "{}-{}-{}".format(self.title,str(self.year),str(self.month))

class WageDetail(models.Model):
    wage                    = models.ForeignKey(Wage,on_delete=models.PROTECT,verbose_name=u"نام لیست")
    employee                = models.ForeignKey(Employee,on_delete=models.PROTECT,verbose_name=u"نام ونام خانوادگی")
    daily_base              = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"‍پایه روزانه")
    work_days               = models.SmallIntegerField(default=0,verbose_name=u"تعداد روز کارکرد")
    absent_days             = models.SmallIntegerField(default=0,verbose_name=u"روز غیبت")
    tiemoff_days            = models.SmallIntegerField(default=0,verbose_name=u"روز مرخصی")
    workdays_in_friday      = models.SmallIntegerField(default=0,verbose_name=u"جمعه کاری")
    workdays_in_holiday     = models.SmallIntegerField(default=0,verbose_name=u"تعطیل کاری")
    work_as_replace         = models.SmallIntegerField(default=0,verbose_name=u"جایگزینی")
    workdays_in_mission     = models.SmallIntegerField(default=0,verbose_name=u"ماموریت")
    is_shift                = models.BooleanField(default=True,verbose_name=u"وضعیت نوبتکاری")
    ovettime_houre          = models.DecimalField(default=0,max_digits=3,decimal_places=3,verbose_name=u"ساعت اضافه کاری")
    children_benefit        = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"حق اولاد")
    monthly_wage_amount     = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"حقوق ماهیانه")
    shift_amount            = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"مبلغ نوبتکاری")
    work_in_holiday_amount  = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"مبلغ تعطیل کاری")
    work_in_friday_amount   = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"مبلغ جمعه کاری")
    work_overtime_amount    = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"مبلغ اضافه کاری")
    work_as_replace_amount  = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"مبلغ جایگزینی")
    commute_amont           = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"مبلغ ایاب و ذهاب")
    bad_wether_right        = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"بدی آب و هوا")
    hygiene_benefit         = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"حق بهداشت")
    food_benefit            = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"حق غذا")
    instruct_amount         = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"مبلغ آموزش")
    backpay_amount          = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"معوق مشمول")
    backpay_tax_exempt      = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"معوق غیر مشمول")
    gross_amount            = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"مبلغ ناخالص")
    tax_include             = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"مشمول مالیات")
    tax_amount              = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"مبلغ مالیات")
    insurance_include       = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"مشمول بیمه")
    insurance_amount        = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"مبلغ بیمه")
    Loan_and_advance        = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"وام و مساعده")
    pay_in_advance          = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"علی الحساب")
    deduction1              = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"سایر کسورات۱")
    deduction2              = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"سایر کسورات ۲")
    net_pay                 = models.DecimalField(default=0,max_digits=11,decimal_places=3,verbose_name=u"خالص پرداختی")
    public_message          = models.TextField(blank=True,null  =True,verbose_name=u"پیام عمومی")
    private_message         = models.TextField(blank=True,null  =True,verbose_name=u"پیام اختصاصی")

    class Meta:
        unique_together=('wage','employee')

    def __str__(self):
        return "{}-{}-{}".format(self.employee,self.wage.year,self.wage.month)
