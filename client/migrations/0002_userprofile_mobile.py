# Generated by Django 3.0.6 on 2020-05-14 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='mobile',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]