from django.urls import path
from truck.views import TruckAPIView


urlpatterns = [
    path("trucks/", TruckAPIView.as_view())
]
