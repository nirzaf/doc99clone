from django.contrib import admin
from .models import Users
from .models import Test

# Register your models here.

admin.site.register(Users)
admin.site.register(Test)
