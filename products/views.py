import random
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from .filter import *


def product_view(request, category_slug , product_slug):
    print(request.user)
    #    cart = Cart(request)

    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)

    #    if request.method == 'POST':
    #        form = AddToCartForm(request.POST)

    #       if form.is_valid():
    #            quantity = form.cleaned_data['quantity']

    #            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)

    #            messages.success(request, 'The product was added to the cart')

    #            return redirect('product', category_slug=category_slug, product_slug=product_slug)
    #   else:
    #       form = AddToCartForm()

    similar_products = list(product.category.products.exclude(id=product.id))

    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)

    return render(
        request,
        'products/productPage.html',
        {
            #            'form': form,
            'product': product,
            'similar_products': similar_products
        },

    )


def search(request):
    print(request.user)
    query = request.GET.get('q', '')
    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    product_filter = ProductFilter(request.GET, queryset=products)
    products = product_filter.qs

    return render(
        request,
        'products/searchPage.html',
        {
            'product_filter': product_filter,
            'products': products,
            'q': query
        }
    )


def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = category.products.all()
    products_a_to_z = category.products.all().order_by('name')
    if request.GET.get('atoz'):
        print("gotten")
        products = category.products.all().order_by('name')
    elif request.GET.get('old'):
        products = category.products.all().order_by('name')
    product_filter = ProductFilter(request.GET, queryset=products)
    products = product_filter.qs
    return render(
        request,
        'products/categoryPage.html',
        {
            'products_a_to_z': products_a_to_z,
            'products': products,
            'product_filter': product_filter,
            'category': category
        },
    )
