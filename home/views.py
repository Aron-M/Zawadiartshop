from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .forms import ProductSearchForm, ProductEditForm
from django.http import JsonResponse

def dashboard(request):
    return render(request, 'dashboard.html')

def edit_product_search(request, product_id=None):
    search_form = ProductSearchForm()
    edit_form = None
    product = None
    products = Product.objects.all()
    total_products = products.count()  # Fetch the total product count

    if request.method == 'GET':
        search_form = ProductSearchForm(request.GET)
        if search_form.is_valid():
            id = search_form.cleaned_data['id']
            try:
                product = Product.objects.get(id=id)
                edit_form = ProductEditForm(instance=product)
            except Product.DoesNotExist:
                product = None

    context = {
        'search_form': search_form,
        'edit_form': edit_form,
        'product': product,
        'products': products,  # Pass all products to the context
        'total_products': total_products,
    }

    return render(request, 'edit_product.html', context)


def delete_product_search(request, product_id=None):
    search_form = ProductSearchForm()
    edit_form = None
    product = None
    products = Product.objects.all()

    # Check if a product_id is provided in the URL
    if product_id:
        product = get_object_or_404(Product, id=product_id)

    if request.method == 'GET':
        search_form = ProductSearchForm(request.GET)
        if search_form.is_valid():  # Corrected line with parentheses
            id = search_form.cleaned_data['id']
            try:
                # Check if the searched product exists and populate the edit form
                product = Product.objects.get(id=id)
                edit_form = ProductEditForm(instance=product)
            except Product.DoesNotExist:
                product = None

    context = {
        'product': product,
        'products': products,
        'search_form': search_form,
    }

    return render(request, 'delete_product.html', context)


def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    total_products = Product.objects.count()  # Get the count of all products

    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=product)
        if edit_form.is_valid():
            edited_product = edit_form.save()
            return redirect('edit_product', product_id=edited_product.id)
    else:
        edit_form = ProductEditForm(instance=product)

    context = {
        'edit_form': edit_form,
        'product': product,
        'total_products': total_products,  # Include the count in the context
    }

    return render(request, 'edit_product.html', context)


def add_product(request):
    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES)
        if edit_form.is_valid():
            new_product = edit_form.save()
            return redirect('new_product_added', new_product.id)
    
    edit_form = ProductEditForm()
    context = {
        'edit_form': edit_form,
    }
    return render(request, 'add_product.html', context)


def new_product_added(request, new_product_id):
    return render(request, 'new_product_added.html', {'new_product_id': new_product_id})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        product.delete()

        # Fetch the updated products list and total count after deleting a product
        products = Product.objects.all()
        total_products = products.count()

        return redirect('dashboard')

    context = {
        'product': product,
        'product_id': product_id,
    }
    return render(request, 'delete_product.html', context)
