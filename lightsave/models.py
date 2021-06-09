from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import AutoField, PositiveIntegerField

# Create your models here.
class User(AbstractUser):
  name = models.CharField(max_length=255, null=True)
  email = models.CharField(max_length=255, unique=True)
  password =models.CharField(max_length=255)
  
  REQUIRED_FIELDS = []

class Appliance(models.Model):
  applianceId = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  wattage= models.PositiveIntegerField()

  
  def __str__(self):
        return self.name

  class Meta:
        ordering = ['pk']  

class CustomAppliance(models.Model):
  applianceId = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  wattage= models.PositiveIntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True)


  def __str__(self):
        return self.name

  class Meta:
        ordering = ['pk'] 
        