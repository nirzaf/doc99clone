from abc import ABC

from rest_framework import serializers
from .models import Users
from .models import Doctors
from .models import Hospitals
from .models import HospitalStaff
from .models import Booking
from .models import Session


class UsersSerializers(serializers.Serializer):
    Id = serializers.IntegerField(allow_null=False)
    First_Name = serializers.CharField(max_length=100)
    Last_Name = serializers.CharField(max_length=100)
    Username = serializers.CharField(max_length=50)
    Password = serializers.CharField(max_length=50)
    Mobile_No = serializers.CharField(max_length=20)
    Auth_Token = serializers.CharField(max_length=200)
    Is_Deleted = serializers.BooleanField(default=True)

    def create(self, validated_data):
        return Users.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.Id = validated_data.get('Id', instance.Id)
        instance.First_Name = validated_data.get('First_Name', instance.First_Name)
        instance.Last_Name = validated_data.get('Last_Name', instance.Last_Name)
        instance.Username = validated_data.get('Username', instance.Username)
        instance.Mobile_No = validated_data.get('Mobile_No', instance.Mobile_No)
        instance.Auth_Token = validated_data.get('Auth_Token', instance.Auth_Token)
        instance.Is_Deleted = validated_data.get('Is_Deleted', instance.Is_Deleted)
        instance.save()
        return instance
