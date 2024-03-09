from msilib.schema import Class
from django.db import models
from django.core.validators import MinLengthValidator





# Create your models here.

class register(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)
    mono=models.IntegerField()
    pin=models.IntegerField()
    pas=models.CharField(max_length=70)
    
class Vehical(models.Model):
    c_name=models.CharField(max_length=70)
    c_no=models.CharField(max_length=10)
    
    
    
