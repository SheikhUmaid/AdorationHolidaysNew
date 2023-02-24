from django.db import models

# Create your models here.

class HeroSubmit(models.Model):
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  phone = models.CharField(max_length=200)
  mail_recieved = models.BooleanField(default = False)
  mail_error = models.TextField(max_length=50000, default = "")
  def __str__(self):
    return str(self.name)

class ContactSubmit(models.Model):
  fname = models.CharField(max_length=200)
  lname = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  message = models.TextField(max_length=50000)
  mail_recieved = models.BooleanField(default = False)
  mail_error = models.TextField(max_length=50000, default = "")
  
  
  def __str__(self):
    return str(self.fname)

class ModelSubmit(models.Model):
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  phone = models.CharField(max_length=200)
  destination = models.CharField(max_length=200)
  mail_recieved = models.BooleanField(default = False)
  mail_error = models.TextField(max_length=50000, default = "")
  
  def __str__(self):
    return str(self.name)