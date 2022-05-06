from django.contrib import admin
from home.models import Images

class Image(admin.ModelAdmin):
    display_field = ('img_name', 'img_date', 'img_image')
admin.site.register(Images, Image)
# Register your models here.
