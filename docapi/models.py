from django.db import models


# Create your models here.
class Users(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_lenght=100)
    Username = models.CharField(max_legnth=50)
    Password = models.CharField(max_length=50)
    Mobile_No = models.CharField(max_length=20)
    Auth_Token = models.CharField(max_length=200)
    Is_Deleted = models.BooleanField(initial=True)
