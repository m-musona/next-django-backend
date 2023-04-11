import graphene
from graphene_django import DjangoObjectType
from .models import Product, Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "title", "slug", "ordering", "tags")


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "name", "description")


class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)

    def resolve_all_products(root, info):
        return Product.objects.all()


schema = graphene.Schema(query=Query)
