from django.shortcuts import render
from django.http import HttpResponse
from products.models import *
from .models import *


def dashboard(request):
    products = Product.objects.all()
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'customers': customers,
        'products': products,
        'total_orders': total_orders,
        'pending': pending,
        'delivered': delivered
    }

    return render(
        request,
        'accounts/dashboard.html',
        context
    )


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()

    context = {
        'customer': customer,
        'orders': orders
    }
    return HttpResponse('customer', context)
