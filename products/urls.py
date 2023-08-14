# products/urls.py

from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('products/', views.products, name='products'),
    # Add URL patterns for other categories (frames, miscellaneous) as needed
]
