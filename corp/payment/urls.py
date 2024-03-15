from django.shortcuts import render
from django.urls import path

from . import views

app_name = 'payment'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('shipping/', views.shipping, name='shipping'),
    path('complete-order/', views.complete_order, name='complete-order'),
    path('payment-success/', views.payment_success, name='payment-success'),
    path('payment-failed/', views.payment_failed, name='payment-failed'),
]