from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .forms import ProductSearchForm, ProductEditForm
import os
import json
from django.http import JsonResponse

JSON_FILE_PATH = '/workspace/Zawadiartshop/products/fixtures/products.json'

# Define a function to load data from the JSON file
def load_product_data():
    product_data = []
    if os.path.exists('/workspace/Zawadiartshop/products/fixtures/products.json'):
        with open('/workspace/Zawadiartshop/products/fixtures/products.json', 'r') as file:
            product_data = json.load(file)
    return product_data

# Define a function to save data to the JSON file
def save_product_data(product_data):
    with open('/workspace/Zawadiartshop/products/fixtures/products.json', 'w') as file:
        print("Saving the following data to the JSON file:")
        print(product_data)
        json.dump(product_data, file, indent=4)

def dashboard(request):
    search_form = ProductSearchForm()
    edit_form = None
    product = None
    products = Product.objects.all()

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
        'products': products,
    }

    return render(request, 'dashboard.html', context)

def edit_product(request, product_id):
    product_data = load_product_data()
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, instance=product)
        if edit_form.is_valid():
            # Update the product data in your JSON data
            for p in product_data:
                if p['pk'] == product_id:
                    cleaned_data = edit_form.cleaned_data

                    # Handle image and origin_image fields separately
                    if 'image' in cleaned_data:
                        cleaned_data['image'] = cleaned_data['image'].url  # Assuming you want to store the image URL
                    if 'origin_image' in cleaned_data:
                        cleaned_data['origin_image'] = cleaned_data['origin_image'].url  # Assuming you want to store the origin image URL

                    p['fields'].update(cleaned_data)
                    break

            # Save the updated product data to the JSON file
            save_product_data(product_data)

            return JsonResponse({'success': True})
        else:
            # Handle form errors and return a JSON response with errors
            errors = edit_form.errors
            return JsonResponse({'success': False, 'errors': errors})
    else:
        edit_form = ProductEditForm(instance=product)

    return render(request, 'dashboard.html', {'edit_form': edit_form, 'product': product})