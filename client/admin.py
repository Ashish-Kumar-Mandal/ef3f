from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from client.models import Contact, UserBank, UserProfile

class ContactAdmin(ModelAdmin):
    list_display = ["name", "mobile", "title", "timeStamp"]
    search_fields = ["title", "message", "mobile"]
    list_filter = ["timeStamp"]
admin.site.register(Contact, ContactAdmin)

class UserBankAdmin(ModelAdmin):
    list_display = ["account_holder_name", "bank_name", "account_number"]
    search_fields = ["account_holder_name", "bank_name", "account_number","ifsc_code"]
    list_filter = ["timeStamp"]
admin.site.register(UserBank, UserBankAdmin)

class UserProfileAdmin(ModelAdmin):
    list_display = ["user_id", "mobile", "my_referal_code", "gender","marital_status", "dob", "timeStamp"]
    search_fields = ["user_id", "mobile", "dob", "designation", "block", "district","state", "pin_code"]
    list_filter = ["timeStamp", "marital_status", "gender"]
admin.site.register(UserProfile, UserProfileAdmin)

