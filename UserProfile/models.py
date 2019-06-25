from django.db import models
from django.contrib.auth.models import User

class UserTableDB(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Fname = models.CharField(max_length=255,null=True)
    Lname = models.CharField(max_length=255,null=True)
    Mobile = models.CharField(max_length=255,null=True)
    Email=   models.CharField(max_length=255,null=True)
    Country = models.CharField(max_length=255,blank=True,null=True)
    State = models.CharField(max_length=255,blank=True,null=True)
    City = models.CharField(max_length=255,blank=True,null=True)
    Address = models.CharField(max_length=10000000, blank=True, null=True)
    Zip = models.CharField(max_length=255,blank=True,null=True)
    Pic = models.TextField(blank=True,null=True)
    ISActive = models.BooleanField(default=False,null=True)
    Activation_Key = models.CharField(max_length=255, blank=True, default='',null=True)
    def __str__(self):
        return (self.Fname)

class ContactUs(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    CompanyName = models.CharField(max_length=100,blank=True,null=True)
    Telephone = models.CharField(max_length=20)
    Message = models.CharField(max_length=3000)
    def __str__(self):
        return (self.Name)
class Subscription(models.Model):

    Email = models.CharField(max_length=100)
    def __str__(self):
        return self.Email