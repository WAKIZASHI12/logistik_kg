from rest_framework_gis.serializers import GeoFeatureModelSerializer

from truck.models import Truck


class TruckSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Truck
        geo_field = "map_schema"
        fields = ("id", "company", "driver")
