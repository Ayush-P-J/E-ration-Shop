from django.db import models
from django.utils import timezone


# from userapp.models import *
# Create your models here.
class Delivery_TB(models.Model):
    Name=models.CharField(max_length=200)
    Address=models.CharField(max_length=30)
    Age=models.CharField(max_length=30)
    Email=models.CharField(max_length=500)
    District=models.CharField(max_length=200)
    Location=models.CharField(max_length=500)
    number=models.CharField(max_length=500)
    Dproof=models.ImageField(upload_to='dproof_DB')
    Mincharge=models.IntegerField()

    Password=models.CharField(max_length=15)

    def __str__(self):
        return self.Name
    

