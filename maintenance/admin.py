from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(ServiceShop)
admin.site.register(ServiceTip)
admin.site.register(Appointment)
