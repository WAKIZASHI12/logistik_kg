from django.db import models
from django.contrib.gis.db import models as geo_models


class Truck(models.Model):
    company = models.CharField(max_length=256)
    driver = models.CharField(max_length=256)
    map_schema = geo_models.LineStringField()
