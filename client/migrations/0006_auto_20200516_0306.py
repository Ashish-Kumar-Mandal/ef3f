# Generated by Django 3.0.6 on 2020-05-15 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_auto_20200516_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Widow', 'Widow'), ('Seprated', 'Seprated'), ('Commited', 'Commited')], default='Single', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
