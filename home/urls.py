# urls.py (in your "home" app)
from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit_product_search/', views.edit_product_search, name='edit_product_search'),
    path('edit_product_search/<int:product_id>/', views.edit_product, name='edit_product_search'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    # path('delete_product_search/', views.edit_product_search, name='edit_product_search'),
    # path('delete_product_search/<int:product_id>/', views.edit_product_search, name='edit_product_search'),
    # path('delete_product/<int:product_id>/', views.delete_product, name='edit_product'),
    # path('add_product_search/<int:product_id>/', views.edit_product_search, name='edit_product_search'),
    # path('add_product/<int:product_id>/', views.add_product, name='edit_product'),
]