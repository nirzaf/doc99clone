from django.urls import path
from .views import users_list, users_detail, GenericUsersAPI, GenericGetUsersAPI
from .views import doctors_list, doctor_details
from .views import hospital_list, hospital_details
from .views import hospital_staff_list, hospital_staff_details
from .views import booking_list, booking_details
from .views import session_list, session_details

urlpatterns = [
    path('users/', users_list),
    path('user_details/<int:pk>/', users_detail),
    path('api/users/', GenericGetUsersAPI.as_view()),
    path('api/users/<int:pk>/', GenericUsersAPI.as_view()),
    path('doctors/', doctors_list),
    path('doctor_details/<int:pk>/', doctor_details),
    path('hospitals/', hospital_list),
    path('hospital_details/<int:pk>/', hospital_details),
    path('staffs/', hospital_staff_list),
    path('staffs_details/<int:pk>/', hospital_staff_details),
    path('bookings/', booking_list),
    path('bookings/<int:pk>/', booking_details),
    path('sessions/', session_list),
    path('sessions/<int:pk>/', session_details),
    path('/', users_list)
]
