from django.urls import path
from .views import GenericUsersAPI, GenericUsersGetAPI
from .views import GenericDoctorsAPI, GenericDoctorsGetAPI
from .views import GenericHospitalAPI, GenericHospitalGetAPI
from .views import GenericHospitalStaffAPI, GenericHospitalStaffGetAPI
from .views import GenericBookingAPI, GenericBookingGetAPI
from .views import GenericSessionAPI, GenericSessionGetAPI

urlpatterns = [
    path('api/users/', GenericUsersGetAPI.as_view()),
    path('api/users/<int:pk>/', GenericUsersAPI.as_view()),
    path('api/doctors/', GenericDoctorsGetAPI.as_view()),
    path('api/doctors/<int:pk>/', GenericDoctorsAPI.as_view()),
    path('api/hospitals/', GenericHospitalGetAPI.as_view()),
    path('api/hospitals/<int:pk>/', GenericHospitalAPI.as_view()),
    path('api/staffs/', GenericHospitalStaffGetAPI.as_view()),
    path('api/staffs/<int:pk>/', GenericHospitalStaffAPI.as_view()),
    path('api/bookings/', GenericBookingGetAPI.as_view()),
    path('api/bookings/<int:pk>/', GenericBookingAPI.as_view()),
    path('api/sessions/', GenericSessionGetAPI.as_view()),
    path('api/sessions/<int:pk>/', GenericSessionAPI.as_view()),
]
