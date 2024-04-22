from django.contrib import admin
from django.contrib.gis import admin as geo_admin
from truck.models import Truck

admin.site.register(Truck, geo_admin.GISModelAdmin)
