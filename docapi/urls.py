from django.urls import path
from .views import users_list
from .views import test_list

urlpatterns = [
    path('users/', users_list),
    path('test/', test_list)
]
