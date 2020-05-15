from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    sn = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    mobile = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    message = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True)


class UserBank(models.Model):
    sn = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    account_holder_name = models.CharField(max_length=100, blank=True, null=True)
    account_number = models.CharField(max_length=30, blank=True, null=True)
    branch_name = models.CharField(max_length=100, blank=True, null=True)
    ifsc_code = models.CharField(max_length=100, blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True)


class UserProfile(models.Model):
    sn = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    use_referal_code = models.CharField(max_length=10, blank=True, null=True)
    my_referal_code = models.CharField(max_length=10, blank=True, null=True)
    mobile = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, default="Male", choices=(("Male","Male"), ("Female","Female")), blank=True, null=True)
    marital_status = models.CharField(max_length=20, default="Single", choices=(("Single","Single"), ("Married","Married"), ("Widow","Widow"), ("Seprated","Seprated"), ("Commited","Commited")), blank=True, null=True)
    dob = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    block = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True) 
    pin_code = models.CharField(max_length=6, blank=True, null=True)
    image = models.ImageField(upload_to="client/users", blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True)

