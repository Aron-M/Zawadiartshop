# urls.py (in your "home" app)
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit_product_by_id/', views.edit_product_search, name='edit_product_by_id'),
    path('edit_product_search/', views.edit_product_search, name='edit_product_search'),  # Keep this for searching
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),  # Keep this for editing
    path('add_product/', views.add_product, name='add_product'),  # Add a new URL pattern for adding a product
    path('new_product_added/<int:new_product_id>/', views.new_product_added, name='new_product_added'),
    path('delete_product_search/', views.delete_product_search, name='delete_product_search'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
]
