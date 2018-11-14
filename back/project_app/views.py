
from .models import Attraction, Town, Order
from rest_framework import viewsets
from .serializers import AttractionSerializer, TownSerializer, OrderSerializer


class AttractionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer


class TownViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Town.objects.all()
    serializer_class = TownSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer