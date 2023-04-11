from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard),
    path('customer/<str:pk>/', views.customer)
]