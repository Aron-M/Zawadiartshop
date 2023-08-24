from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('products/', views.products, name='products'),
    path('paintings/', views.paintings, name='paintings'),
    path('sculptures/', views.sculptures, name='sculptures'),
    path('frames/', views.frames, name='frames'),
    path('crafts/', views.crafts, name='crafts'),
    path('artists/', views.searchmodal, name='artists'),
    path('product_search/', views.product_search, name='product_search'),
]
