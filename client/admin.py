from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from client.models import Contact, UserBank, UserProfile, CompanyBankUPIQR, Membership, Transaction

class ContactAdmin(ModelAdmin):
    list_display = ["name", "mobile", "title", "timeStamp"]
    search_fields = ["title", "message", "mobile"]
    list_filter = ["timeStamp"]
admin.site.register(Contact, ContactAdmin)

class UserBankAdmin(ModelAdmin):
    readonly_fields = ["user_id", "upi_id", "account_number"]
    list_display = ["upi_id", "account_holder_name", "bank_name", "account_number"]
    search_fields = ["account_holder_name", "bank_name", "account_number","ifsc_code"]
    list_filter = ["timeStamp"]
admin.site.register(UserBank, UserBankAdmin)

class UserProfileAdmin(ModelAdmin):
    readonly_fields = ["user_id", "my_referal_code", "use_referal_code"]
    list_display = ["user_id", "mobile", "my_referal_code", "gender", "dob", "timeStamp"]
    search_fields = ["user_id", "mobile", "dob", "block", "district","state", "pin_code"]
    list_filter = ["timeStamp", "gender"]
admin.site.register(UserProfile, UserProfileAdmin)

class CompanyBankUPIQRAdmin(ModelAdmin):
    list_display = ["upi_id", "qr_code", "account_number"]
admin.site.register(CompanyBankUPIQR, CompanyBankUPIQRAdmin)

class MembershipAdmin(ModelAdmin):
    readonly_fields = ['user_id', 'transaction_id','amount', 'txt_date', 'exp_date']
    list_display = ["user_id", "transaction_id", "image_tag", "transaction_slip", "status", "txt_date", "exp_date"]
    search_fields = ["user_id", "transaction_id", "status"]
    list_filter = ["status", "txt_date"]
admin.site.register(Membership, MembershipAdmin)

class TransactionAdmin(ModelAdmin):
    list_display = ["user_id", "transaction_id", "amount", "txt_date", "status"]
    search_fields = ["user_id", "transaction_id", "txt_date", "status"]
    list_filter = ["status", "txt_date"]
admin.site.register(Transaction, TransactionAdmin)