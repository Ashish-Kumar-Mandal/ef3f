# Generated by Django 2.2.12 on 2020-05-28 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0014_auto_20200528_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='status',
            field=models.CharField(blank=True, choices=[('0', 'Inactivated'), ('1', 'Activated')], default='0', max_length=10, null=True),
        ),
    ]
