# Generated by Django 2.2 on 2019-04-19 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseinfo', '0005_auto_20190418_0751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='education_degree',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseinfo.EducationDegree', verbose_name='مدرک تحصیلی'),
        ),
    ]
