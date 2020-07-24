from django.db import models


class Upload(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, null=True, blank=True)
    image = models.ImageField(upload_to='photos/')
