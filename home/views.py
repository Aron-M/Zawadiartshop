from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.urls import reverse
from .forms import ProductSearchForm, ProductEditForm
import os
import json
from django.http import JsonResponse
from products.utils import load_product_data_from_json
import decimal
from decimal import Decimal

JSON_FILE_PATH = '/workspace/Zawadiartshop/products/fixtures/products.json'

# Define a function to load data from the JSON file
def load_product_data():
    product_data = []
    if os.path.exists('/workspace/Zawadiartshop/products/fixtures/products.json'):
        with open('/workspace/Zawadiartshop/products/fixtures/products.json', 'r') as file:
            product_data = json.load(file)
            for product in product_data:
                # Convert the 'price' field to Decimal
                product['fields']['price'] = Decimal(product['fields']['price'])
    return product_data

# Define a function to save data to the JSON file
def save_product_data(product_data):
    for product in product_data:
        product['fields']['price'] = float(product['fields']['price'])
    with open('/workspace/Zawadiartshop/products/fixtures/products.json', 'w') as file:
        print("Saving the following data to the JSON file:")
        print(product_data)
        json.dump(product_data, file, indent=4)

def dashboard(request, product_id=None):
    search_form = ProductSearchForm()
    edit_form = None
    product = None
    product_data = load_product_data_from_json()
    products = Product.objects.all()

    # Check if a product_id is provided in the URL
    if product_id:
        product = get_object_or_404(Product, id=product_id)
        edit_form = ProductEditForm(instance=product)

    if request.method == 'GET':
        search_form = ProductSearchForm(request.GET)
        if search_form.is_valid():
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

    return render(request, 'dashboard.html', context)


def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, instance=product)
        if edit_form.is_valid():
            # Save the updated product to the database
            edit_form.save()
            return redirect('dashboard', product_id=product_id)  # Redirect back to the dashboard_with_product
    else:
        edit_form = ProductEditForm(instance=product)

    context = {
        'edit_form': edit_form,
        'product': product,
    }

    return render(request, 'dashboard.html', context)