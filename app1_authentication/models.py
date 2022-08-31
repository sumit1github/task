from django.db import models
from django.contrib import admin

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=255,blank=True, null=True)

admin.site.register(Product)
