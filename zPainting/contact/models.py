from django.db import models

class Contact(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_subject = models.CharField(max_length=250)
    user_massege = models.CharField(max_length=500)

# Create your models here.
