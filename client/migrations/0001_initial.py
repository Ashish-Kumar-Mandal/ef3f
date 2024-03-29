# Generated by Django 3.0.6 on 2020-05-12 02:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sn', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('mobile', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('sn', models.AutoField(primary_key=True, serialize=False)),
                ('use_referal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('my_referal_code', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=10, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('block', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('pin_code', models.CharField(blank=True, max_length=6, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='client/users')),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserBank',
            fields=[
                ('sn', models.AutoField(primary_key=True, serialize=False)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('account_holder_name', models.CharField(blank=True, max_length=100, null=True)),
                ('account_number', models.CharField(blank=True, max_length=30, null=True)),
                ('branch_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=100, null=True)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
