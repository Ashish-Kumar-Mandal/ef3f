# Generated by Django 2.2.12 on 2020-05-28 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0012_auto_20200528_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]