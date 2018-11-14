from .models import Attraction, Town, Order
from rest_framework import serializers


class AttractionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attraction
        fields = ('name', 'text')


class TownSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Town
        fields = ('name', 'text')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('client_name', 'phone_number', 'order', 'order_date')
