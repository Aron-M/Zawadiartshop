from django.shortcuts import render
from .models import Product


def products(request):
    # Retrieve all products from the database
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)


def searchmodal(request):
    artists = Product.objects.values_list('artist', flat=True).distinct()
    category = Product.objects.values_list('category', flat=True).distinct()
    origin_image = Product.objects.values_list('origin_image', flat=True).distinct()
    origin = Product.objects.values_list('origin', flat=True).distinct()
    origin_code = Product.objects.values_list('origin_code', flat=True).distinct()
    price = Product.objects.values_list('price', flat=True).distinct()
    products = Product.objects.filter(category='origin')
    context = {
               'artists': artists,
               'category': category,
               'origin_image': origin_image,
               'origin': origin,
               'origin_code': origin_code,
               'price': price}
    return render(request, '/workspace/Zawadiartshop/home/templates/homepage.html', context)


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


