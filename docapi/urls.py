from django.urls import path
from .views import users_list

urlpatterns = [
    path('users/', users_list)
]
