from django.shortcuts import render
from .models import Product
from django.template.loader import render_to_string

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


def product_search(request):
    selected_artists = request.GET.getlist('artist')
    selected_categories = request.GET.getlist('category')
    selected_origins = request.GET.getlist('origin')
    selected_origin_images = request.GET.getlist('origin_image')
    max_price = request.GET.get('price')

    artists = Product.objects.values_list('artist', flat=True).distinct()
    category = Product.objects.values_list('category', flat=True).distinct()
    origin_image = Product.objects.values_list('origin_image', 'origin', 'origin_code').distinct()[:6]
    origin = Product.objects.values_list('origin', flat=True).distinct()[:6]
    origin_code = Product.objects.values_list('origin_code', flat=True).distinct()[:6]
    price = Product.objects.values_list('price', flat=True).distinct()

    
    filters = {}

    if selected_artists:
        filters['artist__in'] = selected_artists
    if selected_categories:
        filters['category__in'] = selected_categories
    if selected_origin_images:
        filters['origin_image__in'] = selected_origin_images
    if max_price:
        filters['price__lte'] = max_price

    
    filtered_products = Product.objects.filter(**filters)

    
    filtered_categories = selected_categories
    filtered_artists = selected_artists
    filtered_price = max_price

    
    selected_artist_origins = set()

    
    if selected_artists:
        selected_artist_origins = set(Product.objects.filter(artist__in=selected_artists).values_list('origin', flat=True))

    
    if not selected_artists and selected_categories and selected_origins:
        filtered_products = Product.objects.filter(category__in=selected_categories, origin__in=selected_origins)
        selected_artist_origins.update(selected_origins)

    
    elif not selected_artists and selected_origins:
        filtered_products = Product.objects.filter(origin__in=selected_origins)
        selected_artist_origins.update(selected_origins)

    
    filtered_origin_image_tuples = []
    for origin in selected_artist_origins:
        product_with_origin = Product.objects.filter(origin=origin).first()
        if product_with_origin:
            filtered_origin_image_tuples.append((product_with_origin.origin_image.url, origin))

    
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

    searchmodal_html = render_to_string('layouts/searchbar.html', context, request=request)
    context['searchmodal_html'] = searchmodal_html
    return render(request, 'product_search.html', context)



def products(request):
    products = Product.objects.all()
    artists = Product.objects.values_list('artist', flat=True).distinct()
    category = Product.objects.values_list('category', flat=True).distinct()
    origin_image = Product.objects.values_list('origin_image', 'origin', 'origin_code').distinct()
    origin = Product.objects.values_list('origin', flat=True).distinct()
    origin_code = Product.objects.values_list('origin_code', flat=True).distinct()
    price = Product.objects.values_list('price', flat=True).distinct()
    context = {
        'products': products,
        'artists': artists,
        'category': category,
        'origin_image': origin_image,
        'origin': origin,
        'origin_code': origin_code,
        'price': price
    }
    searchmodal_html = render_to_string('layouts/searchbar.html', context, request=request)
    context['searchmodal_html'] = searchmodal_html
    return render(request, 'products.html', context)


def paintings(request):
    paintings = Product.objects.filter(category='Paintings')
    artists = Product.objects.values_list('artist', flat=True).distinct()
    category = Product.objects.values_list('category', flat=True).distinct()
    origin_image = Product.objects.values_list('origin_image', 'origin', 'origin_code').distinct()
    origin = Product.objects.values_list('origin', flat=True).distinct()
    origin_code = Product.objects.values_list('origin_code', flat=True).distinct()
    price = Product.objects.values_list('price', flat=True).distinct()
    context = {
        'products': paintings,
        'artists': artists,
        'category': category,
        'origin_image': origin_image,
        'origin': origin,
        'origin_code': origin_code,
        'price': price
    }
    searchmodal_html = render_to_string('layouts/searchbar.html', context, request=request)
    context['searchmodal_html'] = searchmodal_html
    return render(request, 'paintings.html', context)


def sculptures(request):
    sculptures = Product.objects.filter(category='Sculptures')
    artists = Product.objects.values_list('artist', flat=True).distinct()
    category = Product.objects.values_list('category', flat=True).distinct()
    origin_image = Product.objects.values_list('origin_image', 'origin', 'origin_code').distinct()
    origin = Product.objects.values_list('origin', flat=True).distinct()
    origin_code = Product.objects.values_list('origin_code', flat=True).distinct()
    price = Product.objects.values_list('price', flat=True).distinct()
    context = {
        'products': sculptures,
        'artists': artists,
        'category': category,
        'origin_image': origin_image,
        'origin': origin,
        'origin_code': origin_code,
        'price': price
    }
    searchmodal_html = render_to_string('layouts/searchbar.html', context, request=request)
    context['searchmodal_html'] = searchmodal_html
    return render(request, 'sculptures.html', context)


def frames(request):
    frames = Product.objects.filter(category='Frames')
    artists = Product.objects.values_list('artist', flat=True).distinct()
    category = Product.objects.values_list('category', flat=True).distinct()
    origin_image = Product.objects.values_list('origin_image', 'origin', 'origin_code').distinct()
    origin = Product.objects.values_list('origin', flat=True).distinct()
    origin_code = Product.objects.values_list('origin_code', flat=True).distinct()
    price = Product.objects.values_list('price', flat=True).distinct()
    context = {
        'products': frames,
        'artists': artists,
        'category': category,
        'origin_image': origin_image,
        'origin': origin,
        'origin_code': origin_code,
        'price': price
    }
    searchmodal_html = render_to_string('layouts/searchbar.html', context, request=request)
    context['searchmodal_html'] = searchmodal_html
    return render(request, 'frames.html', context)


def crafts(request):
    crafts = Product.objects.filter(category='Crafts')
    artists = Product.objects.values_list('artist', flat=True).distinct()
    category = Product.objects.values_list('category', flat=True).distinct()
    origin_image = Product.objects.values_list('origin_image', 'origin', 'origin_code').distinct()
    origin = Product.objects.values_list('origin', flat=True).distinct()
    origin_code = Product.objects.values_list('origin_code', flat=True).distinct()
    price = Product.objects.values_list('price', flat=True).distinct()
    context = {
        'products': crafts,
        'artists': artists,
        'category': category,
        'origin_image': origin_image,
        'origin': origin,
        'origin_code': origin_code,
        'price': price
    }
    searchmodal_html = render_to_string('layouts/searchbar.html', context, request=request)
    context['searchmodal_html'] = searchmodal_html
    return render(request, 'crafts.html', context)


def sale(request):
    sale = Product.objects.filter(status='Sale')
    artists = Product.objects.values_list('artist', flat=True).distinct()
    category = Product.objects.values_list('category', flat=True).distinct()
    origin_image = Product.objects.values_list('origin_image', 'origin', 'origin_code').distinct()
    origin = Product.objects.values_list('origin', flat=True).distinct()
    origin_code = Product.objects.values_list('origin_code', flat=True).distinct()
    price = Product.objects.values_list('price', flat=True).distinct()
    context = {
        'products': sale,
        'artists': artists,
        'category': category,
        'origin_image': origin_image,
        'origin': origin,
        'origin_code': origin_code,
        'price': price,
        
    }
    searchmodal_html = render_to_string('layouts/searchbar.html', context, request=request)
    context['searchmodal_html'] = searchmodal_html
    return render(request, 'sale.html', context)