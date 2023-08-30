from django.shortcuts import render
from .models import Product
from django.db.models import Q
from django.template.loader import render_to_string


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
        'price': price
    }
    searchmodal_html = render_to_string('layouts/searchbar.html', context, request=request)
    context['searchmodal_html'] = searchmodal_html
    return render(request, 'homepage.html', context)


from django.shortcuts import render
from django.template.loader import render_to_string
from .models import Product

def product_search(request):
    selected_artists = request.GET.getlist('artist')
    selected_categories = request.GET.getlist('category')
    selected_origins = request.GET.getlist('origin')
    selected_origin_images = request.GET.getlist('origin_image')
    max_price = request.GET.get('price')

    artists = Product.objects.values_list('artist', flat=True).distinct()
    category = Product.objects.values_list('category', flat=True).distinct()
    origin_image = Product.objects.values_list('origin_image', 'origin', 'origin_code').distinct()
    origin = Product.objects.values_list('origin', flat=True).distinct()
    origin_code = Product.objects.values_list('origin_code', flat=True).distinct()
    price = Product.objects.values_list('price', flat=True).distinct()

    # Create a dictionary to hold the filter conditions
    filters = {}

    if selected_artists:
        filters['artist__in'] = selected_artists
    if selected_categories:
        filters['category__in'] = selected_categories
    if selected_origin_images:
        filters['origin_image__in'] = selected_origin_images
    if max_price:
        filters['price__lte'] = max_price

    # Apply the filters to the queryset
    filtered_products = Product.objects.filter(**filters)

    # Prepare filter values for the summary
    filtered_categories = selected_categories
    filtered_artists = selected_artists
    filtered_price = max_price

    # Prepare a set to hold the origins of selected artists
    selected_artist_origins = set()

    # Filter products by selected artists and get their origins
    if selected_artists:
        selected_artist_origins = set(Product.objects.filter(artist__in=selected_artists).values_list('origin', flat=True))

    # Prepare origin image tuples
    filtered_origin_image_tuples = []
    for origin in selected_artist_origins:
        product_with_origin = Product.objects.filter(origin=origin).first()
        if product_with_origin:
            filtered_origin_image_tuples.append((product_with_origin.origin_image.url, origin))

    # Prepare origins not matching selected artists
    origins_not_matching_artists = [origin for origin in selected_origins if origin not in selected_artist_origins]

    context = {
        'filtered_products': filtered_products,
        'filtered_categories': filtered_categories,
        'filtered_origins': selected_artist_origins,
        'filtered_origin_image_tuples': filtered_origin_image_tuples,
        'filtered_artists': filtered_artists,
        'filtered_price': filtered_price,
        'origins_not_matching_artists': origins_not_matching_artists,
        'artists': artists,
        'category': category,
        'origin_image': origin_image,
        'origin': origin,
        'origin_code': origin_code,
        'price': price
    }

    # If only origin is selected
    if not selected_artists and selected_origins:
        origin_products = Product.objects.filter(origin__in=selected_origins)
        origin_artists = set(Product.objects.filter(origin__in=selected_origins).values_list('artist', flat=True))
        
        # Update filtered_products with origin products
        filtered_products = origin_products

        # Update selected_artist_origins with selected origins
        selected_artist_origins.update(selected_origins)

        context['artists_of_selected_origins'] = origin_artists
        context['selected_origins'] = selected_origins

    # Render the searchmodal template to a string
    searchmodal_html = render_to_string('/workspace/Zawadiartshop/templates/layouts/searchbar.html', context)

    # Add the searchmodal HTML to the context
    context['searchmodal_html'] = searchmodal_html

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


