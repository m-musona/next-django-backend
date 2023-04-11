import random

from django.shortcuts import render
from django.http import HttpResponse
from products.models import *
from rest_framework.response import *
from rest_framework.decorators import api_view


# Create your views here.
def home(request):
    products = Product.objects.all()
    featured_products = Product.objects.all()[0:8]

    context = {
        'featured_products': featured_products,
        'products': products
    }
    return render(
        request,
        'home/homePage.html',
        context
    )

@api_view(['GET'])
def getRoutes(request):

    routes = [

    ]
    return Response(routes,)
