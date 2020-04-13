from django.http import JsonResponse
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Booking
from .models import Doctors
from .models import HospitalStaff
from .models import Hospitals
from .models import Session
from .models import Users
from .serializers import BookingSerializers
from .serializers import DoctorsSerializers
from .serializers import HospitalSerializers
from .serializers import HospitalStaffSerializers
from .serializers import SessionSerializers
from .serializers import UsersSerializers


# Create your views here.
class GenericUsersAPI(generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin):
    serializer_class = UsersSerializers
    queryset = Users.objects.all()

    lookup_field = 'pk'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        return self.retrieve(request, pk=pk)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)


class GenericUsersGetAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = UsersSerializers
    queryset = Users.objects.all()

    def get(self, request):
        return self.list(request)


class GenericDoctorsAPI(generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin):
    serializer_class = DoctorsSerializers
    queryset = Doctors.objects.all()

    lookup_field = 'pk'

    def get(self, request, pk=None):
        return self.retrieve(request, pk=pk)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)


class GenericDoctorsGetAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = DoctorsSerializers
    queryset = Doctors.objects.all()

    def get(self, request):
        return self.list(request)


class GenericHospitalAPI(generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                         mixins.RetrieveModelMixin):
    serializer_class = HospitalSerializers
    queryset = Hospitals.objects.all()

    lookup_field = 'pk'

    def get(self, request, pk=None):
        return self.retrieve(request, pk=pk)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)


class GenericHospitalGetAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = HospitalSerializers
    queryset = Hospitals.objects.all()

    def get(self, request):
        return self.list(request)


class GenericHospitalStaffAPI(generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                              mixins.RetrieveModelMixin):
    serializer_class = HospitalStaffSerializers
    queryset = HospitalStaff.objects.all()

    lookup_field = 'pk'

    def get(self, request, pk=None):
        return self.retrieve(request, pk=pk)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)


class GenericHospitalStaffGetAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = HospitalStaffSerializers
    queryset = HospitalStaff.objects.all()

    def get(self, request):
        return self.list(request)


class GenericBookingAPI(generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin):
    serializer_class = BookingSerializers
    queryset = Booking.objects.all()

    lookup_field = 'pk'

    def get(self, request, pk=None):
        return self.retrieve(request, pk=pk)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)


class GenericBookingGetAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = BookingSerializers
    queryset = Booking.objects.all()

    def get(self, request):
        return self.list(request)


class GenericSessionAPI(generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin):
    serializer_class = SessionSerializers
    queryset = Session.objects.all()

    lookup_field = 'pk'

    def get(self, request, pk=None):
        return self.retrieve(request, pk=pk)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)


class GenericSessionGetAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = HospitalStaffSerializers
    queryset = HospitalStaff.objects.all()

    def get(self, request):
        return self.list(request)


"""
@api_view(['GET', 'POST'])
def users_list(request):
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UsersSerializers(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UsersSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def users_detail(request, pk):
    try:
        user = Users.objects.get(pk=pk)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsersSerializers(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsersSerializers(user, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def doctors_list(request):
    if request.method == 'GET':
        doctors = Doctors.objects.all()
        doctorsSerializer = DoctorsSerializers(doctors, many=True)
        return Response(doctorsSerializer.data)

    elif request.method == 'POST':
        serializer = DoctorsSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def doctor_details(request, pk):
    try:
        doctor = Doctors.objects.get(pk=pk)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        doctors = Doctors.objects.all()
        doctorsSerializer = DoctorsSerializers(doctors, many=True)
        return Response(doctorsSerializer.data)

    elif request.method == 'PUT':
        serializer = DoctorsSerializers(doctor, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def hospital_list(request):
    if request.method == 'GET':
        hospital = Hospitals.objects.all()
        hospitalSerializer = HospitalSerializers(hospital, many=True)
        return JsonResponse(hospitalSerializer.data, safe=False)

    elif request.method == 'POST':
        serializer = HospitalSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def hospital_details(request, pk):
    try:
        hospital = Hospitals.objects.get(pk=pk)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        hospitals = Hospitals.objects.all()
        hospitalSerializer = HospitalSerializers(hospitals, many=True)
        return Response(hospitalSerializer.data)

    elif request.method == 'PUT':
        serializer = HospitalSerializers(hospital, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def hospital_staff_list(request):
    if request.method == 'GET':
        staff = HospitalStaff.objects.all()
        staffSerializers = HospitalStaffSerializers(staff, many=True)
        return Response(staffSerializers.data)

    elif request.method == 'POST':
        serializer = HospitalStaffSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def hospital_staff_details(request, pk):
    try:
        staff = HospitalStaff.objects.get(pk=pk)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        staff = HospitalStaff.objects.all()
        staffSerializers = HospitalStaffSerializers(staff, many=True)
        return Response(staffSerializers.data)

    elif request.method == 'PUT':
        serializer = HospitalStaffSerializers(staff, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def booking_list(request):
    if request.method == 'GET':
        book = Booking.objects.all()
        bookingSerializer = BookingSerializers(book, many=True)
        return Response(bookingSerializer.data)

    elif request.method == 'POST':
        serializer = BookingSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def booking_details(request, pk):
    try:
        booking = Booking.objects.get(pk=pk)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        book = Booking.objects.all()
        bookingSerializer = BookingSerializers(book, many=True)
        return Response(bookingSerializer.data)

    elif request.method == 'PUT':
        serializer = BookingSerializers(booking, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def session_list(request):
    if request.method == 'GET':
        session = Session.objects.all()
        sessionSerializer = SessionSerializers(session, many=True)
        return Response(sessionSerializer.data)

    elif request.method == 'POST':
        serializer = SessionSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def session_details(request, pk):
    try:
        session = Session.objects.get(pk=pk)
    except Exception:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        session = Session.objects.all()
        sessionSerializer = SessionSerializers(session, many=True)
        return Response(sessionSerializer.data)

    elif request.method == 'PUT':
        serializer = SessionSerializers(session, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    """
