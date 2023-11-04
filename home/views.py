from django.shortcuts import render, get_object_or_404
from products.models import Product
from .forms import ProductSearchForm, ProductEditForm


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


def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductEditForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = ProductEditForm(instance=product)

    return render(request, 'edit_product.html', {'form': form})