# products/urls.py

from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.products_view, name='products'),
    path('paintings/', views.paintings_view, name='paintings'),
    path('sculptures/', views.sculptures_view, name='sculptures'),
    # Add URL patterns for other categories (frames, miscellaneous) as needed
]
