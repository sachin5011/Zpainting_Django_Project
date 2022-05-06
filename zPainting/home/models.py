from django.db import models

class Images(models.Model):
    img_name = models.CharField(max_length=100)
    img_date = models.DateTimeField()
    img_image = models.FileField(upload_to='images/', max_length=150, null=False, default=None)
# Create your models here.
