from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout_view, name='checkout'),
    path('checkout/', views.checkout_product_view, name='product_checkout'),
    path('confirmation/', views.confirmation_view, name='confirmation'),
]
