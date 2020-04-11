from django.db import models
from datetime import datetime


# Create your models here.
class Users(models.Model):
    Id = models.BigIntegerField(primary_key=True)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    Mobile_No = models.CharField(max_length=20)
    Auth_Token = models.CharField(max_length=200)
    Is_Deleted = models.BooleanField(default=True)

    def __str__(self):
        return "User with Id Number : " + str(self.Id) + " is added!"


class Doctors(models.Model):
    Id: int = models.BigIntegerField(primary_key=True)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Mobile_No = models.CharField(max_length=20)
    Category = models.CharField(max_length=200)
    Is_Deleted = models.BooleanField(default=True)

    def __str__(self):
        return str("Dr." + self.First_Name + " " + self.Last_Name + " is added successfully!")


class Hospitals(models.Model):
    Id: int = models.BigIntegerField(primary_key=True)
    Name = models.CharField(max_length=200)
    Address = models.TextField(max_length=256)
    Telephone = models.CharField(max_length=20)
    Email = models.EmailField(max_length=100)
    Is_Deleted = models.BooleanField(default=True)

    def __str__(self):
        return self.Name + " is added successfully!"


class HospitalStaff(models.Model):
    Id: int = models.BigIntegerField(primary_key=True)
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Address = models.TextField(max_length=256)
    StaffId = models.CharField(max_length=50)
    User_Type = models.IntegerField(default=0)
    Hospital_Id = models.ForeignKey(Hospitals, on_delete=models.CASCADE)
    Is_Deleted = models.BooleanField(default=True)

    def __str__(self):
        return self.First_Name + " " + self.Last_Name + " is added successfully!"


class Session(models.Model):
    Session_Id: str = models.CharField(max_length=100, primary_key=True)
    Date = models.DateField(default=datetime.now)
    Slot_Begin = models.CharField(max_length=10)
    Slot_End = models.CharField(max_length=10)
    Max_Limit = models.IntegerField(default=0)
    Is_Deleted = models.BooleanField(default=True)

    def __str__(self):
        return "Session created successfully with Session Id " + self.Session_Id


class Booking(models.Model):
    Booking_Id = models.BigIntegerField(primary_key=True)
    Booked_By = models.IntegerField(default=0)
    User_Id = models.ForeignKey(Users, on_delete=models.CASCADE)
    Session_Id = models.ForeignKey(Session, models.CASCADE)
    Is_Paid = models.BooleanField(default=False)
    Is_Canceled = models.BooleanField(default=False)
    Is_Deleted = models.BooleanField(default=True)

    def __str__(self):
        return str(self.Booking_Id)

