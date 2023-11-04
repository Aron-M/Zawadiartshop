# urls.py (in your "home" app)
from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('dashboard/', views.dashboard, name='dashboard'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
]