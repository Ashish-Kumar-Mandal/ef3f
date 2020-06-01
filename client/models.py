from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.html import mark_safe

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
    upi_id = models.CharField(max_length=50, blank=True, null=True)
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
    mobile = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=10, default="Male", choices=(("Male","Male"), ("Female","Female")), blank=True, null=True)
    dob = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    block = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True) 
    pin_code = models.CharField(max_length=6, blank=True, null=True)
    image = models.ImageField(upload_to="client/users", blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True)


class CompanyBankUPIQR(models.Model):
    sn = models.AutoField(primary_key=True)
    pay_ammount = models.CharField(max_length=10, blank=True, null=True)
    upi_id = models.CharField(max_length=30, blank=True, null=True)
    qr_code = models.ImageField(upload_to="client/qrcode", blank=True, null=True)
    account_holder_name = models.CharField(max_length=30, blank=True, null=True)
    account_number = models.CharField(max_length=30, blank=True, null=True)
    bank_name = models.CharField(max_length=60, blank=True, null=True)
    branch_name = models.CharField(max_length=100, blank=True, null=True)
    ifsc_code = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(auto_now_add=True)


class Membership(models.Model):
    Membership_id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    transaction_slip = models.ImageField(upload_to="client/transactionSlip", blank=True, null=True)
    amount = models.CharField(max_length=5, blank=True, null=True)
    status = models.CharField(max_length=10, default="0", choices=(("0","Inactivated"), ("1","Activated")), blank=True, null=True)
    txt_date = models.DateField(blank=True, null=True)
    exp_date = models.DateField(blank=True, null=True)

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.transaction_slip))

    image_tag.short_description = 'Slip'

  
class Transaction(models.Model):
    sn = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    amount = models.CharField(max_length=10, blank=True, null=True)
    upi_or_account = models.CharField(max_length=30, blank=True, null=True)
    txt_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, default="1", choices=(("0","Failed"), ("1","Success")), blank=True, null=True)
