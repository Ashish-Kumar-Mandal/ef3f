# Generated by Django 3.0.6 on 2020-05-14 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_userprofile_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]