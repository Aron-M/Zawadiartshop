from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # URL pattern for the homepage
    path('', views.homepage_view, name='home'),
    # Add more URL patterns for other pages as needed
]