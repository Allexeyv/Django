import graphene

from graphene_django.types import DjangoObjectType

from .models import Attraction, Town, Order


class AttractionType(DjangoObjectType):
    class Meta:
        model = Attraction


class TownType(DjangoObjectType):
    class Meta:
        model = Town


class OrderType(DjangoObjectType):
    class Meta:
        model = Order


class Query(object):
    all_attractions = graphene.List(AttractionType)
    all_towns = graphene.List(TownType)
    all_orders = graphene.List(OrderType)

    attraction = graphene.Field(AttractionType,
                                id=graphene.Int(),
                                name=graphene.String(),
                                town=graphene.String())
    town = graphene.Field(TownType,
                          id=graphene.Int(),
                          name=graphene.String())
    order = graphene.Field(OrderType,
                           id=graphene.Int(),
                           client_name=graphene.String(),
                           phone_number=graphene.String())

    def resolve_all_attractions(self, info, **kwargs):
        return Attraction.objects.all()

    def resolve_all_towns(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Town.objects.all()

    def resolve_all_orders(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Order.objects.all()

    def resolve_attraction(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        town = kwargs.get('town')

        if id is not None:
            return Attraction.objects.get(pk=id)

        if name is not None:
            return Attraction.objects.get(name=name)

        if town is not None:
            return Attraction.objects.get(town=town)

        return None

    def resolve_town(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Town.objects.get(pk=id)

        if name is not None:
            return Town.objects.get(name=name)

        return None

    def resolve_order(self, info, **kwargs):
        id = kwargs.get('id')
        client_name = kwargs.get('client_name')
        phone_number = kwargs.get('phone_number')

        if id is not None:
            return Order.objects.get(pk=id)

        if name is not None:
            return Order.objects.get(client_name=client_name)

        if name is not None:
            return Order.objects.get(phone_number=phone_number)

        return None