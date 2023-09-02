from django.urls import path
from . import views


urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
]
