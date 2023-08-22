# products/urls.py

from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('products/', views.products, name='products'),
    path('paintings/', views.paintings, name='paintings'),
    path('sculptures/', views.sculptures, name='sculptures'),
    path('frames/', views.frames, name='frames'),
    path('crafts/', views.crafts, name='crafts'),
    path('home/', views.artists, name='artists'),
]
