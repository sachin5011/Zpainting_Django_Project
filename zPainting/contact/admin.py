from django.contrib import admin
from .models import Contact
class UserContact(admin.ModelAdmin):
    display_field = ('user_name', 'user_email', 'user_subject', 'user_massege')
admin.site.register(Contact, UserContact)
# Register your models here.
