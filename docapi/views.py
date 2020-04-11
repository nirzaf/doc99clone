from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Users
from .models import Doctors
from .models import Hospitals
from .models import HospitalStaff
from .models import Session
from .models import Booking

from .serializers import UsersSerializers
from .serializers import DoctorsSerializers
from .serializers import HospitalSerializers
from .serializers import HospitalStaffSerializers
from .serializers import BookingSerializers
from .serializers import SessionSerializers


# Create your views here.
@csrf_exempt
def users_list(request):
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UsersSerializers(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsersSerializers(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=404)


@csrf_exempt
def doctors_list(request):
    if request.method == 'GET':
        doctors = Doctors.objects.all()
        doctorsSerializer = DoctorsSerializers(doctors, many=True)
        return JsonResponse(doctorsSerializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsersSerializers(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=404)


@csrf_exempt
def hospital_list(request):
    if request.method == 'GET':
        hospital = Hospitals.objects.all()
        hospitalSerializer = HospitalSerializers(hospital, many=True)
        return JsonResponse(hospitalSerializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsersSerializers(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=404)


@csrf_exempt
def hospital_staff_list(request):
    if request.method == 'GET':
        staff = HospitalStaff.objects.all()
        staffSerializers = HospitalStaffSerializers(staff, many=True)
        return JsonResponse(staffSerializers.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsersSerializers(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=404)


@csrf_exempt
def booking_list(request):
    if request.method == 'GET':
        book = Booking.objects.all()
        bookingSerializer = BookingSerializers(book, many=True)
        return JsonResponse(bookingSerializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsersSerializers(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=404)


@csrf_exempt
def session_list(request):
    if request.method == 'GET':
        session = Session.objects.all()
        sessionSerializer = SessionSerializers(session, many=True)
        return JsonResponse(sessionSerializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsersSerializers(data=data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=404)