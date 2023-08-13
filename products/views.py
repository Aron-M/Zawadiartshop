# products/views.py

from django.shortcuts import render
from .models import Product


def products(request):
    # Retrieve all products from the database
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/templates/products.html', context)


def paintings(request):
    # Retrieve products with the 'paintings' category from the database
    paintings = Product.objects.filter(category='paintings')
    context = {'products': paintings, 'category': 'Paintings'}
    return render(request, 'products/templates/category.html', context)


def sculptures(request):
    # Retrieve products with the 'sculptures' category from the database
    sculptures = Product.objects.filter(category='sculptures')
    context = {'products': sculptures, 'category': 'Sculptures'}
    return render(request, 'products/templates/category.html', context)

# Add views for other categories (frames, miscellaneous) as needed
