from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout_view, name='checkout'),
    path('confirmation/', views.confirmation_view, name='confirmation'),
]
