from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_view, name='product'),
    path('<slug:category_slug>/', views.category, name='category')
]
