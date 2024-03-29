# Generated by Django 3.0.6 on 2020-05-15 20:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_auto_20200514_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('single', 'single'), ('married', 'married'), ('widow', 'widow'), ('seprated', 'seprated'), ('commited', 'commited')], default='single', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')]),
        ),
    ]
