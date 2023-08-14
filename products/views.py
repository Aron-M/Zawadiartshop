from django.shortcuts import render
from .models import Product


def products(request):
    # Retrieve all products from the database
    products = Product.objects.all()
    context = {'product': products}
    return render(request, 'products.html', context)


