from django.shortcuts import render, redirect


def products(request):
    # This view will render the main products template
    return render(request, '/workspace/Zawadiartshop/products/templates/products.html')


def paintings(request):
    # This view will render the template for the 'paintings' category
    return render(request, 'products/category.html', {'category': 'Paintings'})


def sculptures(request):
    # This view will render the template for the 'sculptures' category
    return render(request, 'products/category.html', {'category': 'Sculptures'})

