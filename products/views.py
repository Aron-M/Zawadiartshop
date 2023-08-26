from django.shortcuts import render
from .models import Product
from django.db.models import Q


def products(request):
    # Retrieve all products from the database
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)


def searchmodal(request):
    artists = Product.objects.values_list('artist', flat=True).distinct()
    category = Product.objects.values_list('category', flat=True).distinct()
    origin_image = Product.objects.values_list('origin_image', 'origin', 'origin_code').distinct()
    origin = Product.objects.values_list('origin', flat=True).distinct()
    origin_code = Product.objects.values_list('origin_code', flat=True).distinct()
    price = Product.objects.values_list('price', flat=True).distinct()
    context = {
               'artists': artists,
               'category': category,
               'origin_image': origin_image,
               'origin': origin,
               'origin_code': origin_code,
               'price': price}
    return render(request, 'homepage.html', context)


def product_search(request):
    selected_artists = request.GET.getlist('artist')
    selected_categories = request.GET.getlist('category')
    selected_origins = request.GET.getlist('origin')
    max_price = request.GET.get('price')

    # Create a dictionary to hold the filter conditions
    filters = {}

    if selected_artists:
        filters['artist__in'] = selected_artists
    if selected_categories:
        filters['category__in'] = selected_categories
    if selected_origins:
        filters['origin__in'] = selected_origins
    if max_price:
        filters['price__lte'] = max_price

    # Apply the filters to the queryset
    filtered_products = Product.objects.filter(**filters)

    # Prepare filter values for the summary
    filtered_categories = selected_categories
    filtered_origins = selected_origins
    filtered_artists = selected_artists
    filtered_price = max_price

    context = {
        'filtered_products': filtered_products,
        'filtered_categories': filtered_categories,
        'filtered_origins': filtered_origins,
        'filtered_artists': filtered_artists,
        'filtered_price': filtered_price,
    }
    return render(request, 'product_search.html', context)


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


