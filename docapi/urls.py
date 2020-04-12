from django.urls import path
from .views import users_list
from .views import doctors_list
from .views import hospital_list
from .views import hospital_staff_list
from .views import booking_list
from .views import session_list

urlpatterns = [
    path('users/', users_list),
    path('doctors/', doctors_list),
    path('hospitals/', hospital_list),
    path('staffs/', hospital_staff_list),
    path('bookings/', booking_list),
    path('sessions/', session_list),
    path('/', users_list)
]
