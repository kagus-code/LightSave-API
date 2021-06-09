from django.contrib import admin
from .models import User,Appliance,CustomAppliance
# Register your models here.
admin.site.register(User)
admin.site.register(Appliance)
admin.site.register(CustomAppliance)