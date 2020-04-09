from abc import ABC

from rest_framework import serializers
from .models import Users
from .models import Doctors
from .models import Hospitals
from .models import HospitalStaff
from .models import Booking
from .models import Session


class UsersSerializers(serializers.Serializer):
    Id = serializers.BigIntegerField(primary_key=True)
    First_Name = serializers.CharField(max_length=100)
    Last_Name = serializers.CharField(max_length=100)
    Username = serializers.CharField(max_length=50)
    Password = serializers.CharField(max_length=50)
    Mobile_No = serializers.CharField(max_length=20)
    Auth_Token = serializers.CharField(max_length=200)
    Is_Deleted = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Users.objects.create(validated_data)
