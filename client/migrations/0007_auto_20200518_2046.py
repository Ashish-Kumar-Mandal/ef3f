# Generated by Django 3.0.6 on 2020-05-18 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_auto_20200516_0306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='marital_status',
        ),
    ]
