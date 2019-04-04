# Generated by Django 2.2 on 2019-04-03 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseinfo', '0008_postplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('fathername', models.CharField(max_length=50)),
                ('national_code', models.CharField(max_length=10)),
                ('id_number', models.CharField(max_length=10)),
                ('insurance_id', models.CharField(max_length=10)),
                ('children_count', models.IntegerField()),
                ('tax_exempt', models.BooleanField(default=False)),
                ('indsurence_exempt', models.BooleanField(default=False)),
                ('tel', models.CharField(blank=True, max_length=19)),
                ('mobile', models.CharField(blank=True, max_length=19)),
                ('employee_status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='baseinfo.EmployeeStatus')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='baseinfo.Employer')),
                ('marital_status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='baseinfo.MaritalStatus')),
                ('post_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseinfo.PostPlace')),
                ('work_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseinfo.WorkGroup')),
                ('work_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseinfo.WorkPlace')),
                ('work_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='baseinfo.WorkStatus')),
            ],
        ),
    ]