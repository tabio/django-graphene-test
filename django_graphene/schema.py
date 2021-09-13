import graphene
from graphene_django import DjangoObjectType

from .models import Staff, Store


class StoreType(DjangoObjectType):
    class Meta:
        model = Store


class StaffType(DjangoObjectType):
    class Meta:
        model = Staff


class Query(graphene.ObjectType):
    stores = graphene.List(StoreType)
    staffs = graphene.List(StaffType)

    def resolve_stores(self, info, **kwargs):
        return Store.objects.all()

    def resolve_staffs(self, info, **kwargs):
        return Staff.objects.all()


schema = graphene.Schema(query=Query)
