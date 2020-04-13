from rest_framework import serializers
from .models import Users
from .models import Hospitals
from .models import Doctors
from .models import HospitalStaff
from .models import Session
from .models import Booking


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class DoctorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = '__all__'


class HospitalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hospitals
        fields = '__all__'


class HospitalStaffSerializers(serializers.ModelSerializer):
    class Meta:
        model = HospitalStaff
        fields = '__all__'


class SessionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
