from django.contrib import admin
from .models import Users
from .models import Doctors
from .models import Hospitals
from .models import HospitalStaff
from .models import Booking
from .models import Session

# Register your models here.

admin.site.register(Users)
admin.site.register(Doctors)
admin.site.register(HospitalStaff)
admin.site.register(Hospitals)
admin.site.register(Booking)
admin.site.register(Session)