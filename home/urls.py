from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for the homepage
    path('', views.homepage_view, name='homepage'),
    # Add more URL patterns for other pages as needed
]