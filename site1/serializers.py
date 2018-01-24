from .models import Attractions, Towns
from rest_framework import serializers


class AttractionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attractions
        fields = ('name', 'text')


class TownsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Towns
        fields = ('name', 'text')