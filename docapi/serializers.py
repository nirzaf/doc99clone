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
        fields = ['Id', 'First_Name', 'Last_Name', 'Username', 'Password', 'Mobile_No', 'Auth_Token', 'Is_Deleted']


class DoctorsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = ['Id', 'First_Name', 'Last_Name', 'Mobile_No', 'Category', 'Is_Deleted']


class HospitalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hospitals
        fields = ['Id', 'Name', 'Address', 'Telephone', 'Email', 'Is_Deleted']


class HospitalStaffSerializers(serializers.ModelSerializer):
    class Meta:
        model = HospitalStaff
        fields = ['Id', 'Username', 'Password', 'First_Name', 'Last_Name', 'Address', 'StaffId', 'User_Type',
                  'Hospital_Id', 'Is_Deleted']


class SessionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['Session_Id', 'Date', 'Slot_Begin', 'Slot_End', 'Max_Limit', 'Is_Deleted']


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['Booking_Id', 'Booked_By', 'User_Id', 'Session_Id', 'Session_Id', 'Is_Paid','Is_Canceled', 'Is_Deleted']

