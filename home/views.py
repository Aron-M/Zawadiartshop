from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .forms import ProductSearchForm, ProductEditForm

def dashboard(request):
    return render(request, 'dashboard.html')

def edit_product_search(request, product_id=None):
    search_form = ProductSearchForm()
    edit_form = None
    product = None
    products = Product.objects.all()

    # Check if a product_id is provided in the URL
    if product_id:
        product = get_object_or_404(Product, id=product_id)
        edit_form = ProductEditForm(instance=product)

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
        'search_form': search_form,
        'edit_form': edit_form,
        'product': product,
        'products': products,
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

def add_product(request):
    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES)
        if edit_form.is_valid():
            # Save the new product
            new_product = edit_form.save()
            return redirect('edit_product', product_id=new_product.id)

    else:
        edit_form = ProductEditForm()

    context = {
        'edit_form': edit_form,
    }

    return render(request, 'add_product.html', context)

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

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
    }

    return render(request, 'edit_product.html', context)

def delete_product(request, product_id):
    # Get the product to delete, or return a 404 response if it doesn't exist
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        # If the request is a POST request, delete the product
        product.delete()
        return redirect('dashboard')  # Redirect to the dashboard or another appropriate page

    # Render a confirmation template for the delete action
    context = {'product': product,
               'product_id': product_id,
    }
    return render(request, 'delete_product.html', context)
