from django.contrib import admin
from .models import VehicleOwned


class VehicleOwnedAdmin(admin.ModelAdmin):
    model = VehicleOwned

admin.site.register(VehicleOwned, VehicleOwnedAdmin)

