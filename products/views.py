from django.shortcuts import render
from .models import Product


def products(request):
    # Retrieve all products from the database
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)


def paintings(request):
    paintings = Product.objects.filter(category='Paintings')
    return render(request, 'paintings.html', {'products': paintings})


def sculptures(request):
    sculptures = Product.objects.filter(category='Sculptures')
    return render(request, 'sculptures.html', {'products': sculptures})


def frames(request):
    frames = Product.objects.filter(category='Frames')
    return render(request, 'frames.html', {'products': frames})


def crafts(request):
    crafts = Product.objects.filter(category='Crafts')
    return render(request, 'crafts.html', {'products': crafts})
