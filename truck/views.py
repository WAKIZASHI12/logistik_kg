from rest_framework.generics import ListAPIView

from truck.models import Truck
from truck.serializers import TruckSerializer


class TruckAPIView(ListAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
