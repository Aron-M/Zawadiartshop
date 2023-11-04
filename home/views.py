from django.shortcuts import render, get_object_or_404
from products.models import Product
from .forms import ProductSearchForm


def dashboard(request):
    form = ProductSearchForm()
    product = None
    products = Product.objects.all()

    if request.method == 'GET':
        form = ProductSearchForm(request.GET)
        if form.is_valid():
            id = form.cleaned_data['id']
            try:
                product = Product.objects.get(id=id)
            except Product.DoesNotExist:
                product = None

    context = {
        'form': form,
        'product': product,
        'products': products,
    }

    return render(request, 'dashboard.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_card.html', {'product': product})