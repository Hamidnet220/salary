# Generated by Django 2.2 on 2019-04-03 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseinfo', '0005_bank'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('child_benefit', models.DecimalField(decimal_places=2, max_digits=50)),
                ('dwelling_benefit', models.DecimalField(decimal_places=2, max_digits=50)),
                ('Bon_benefit', models.DecimalField(decimal_places=2, max_digits=50)),
            ],
        ),
    ]
