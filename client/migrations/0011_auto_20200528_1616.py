# Generated by Django 2.2.12 on 2020-05-28 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0010_companybankupiqr_membership_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='exp_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='membership',
            name='txt_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
