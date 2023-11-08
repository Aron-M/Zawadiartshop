from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from products.models import Product
from django.urls import reverse
from .forms import ProductSearchForm, ProductEditForm
import os


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

    return render(request, 'edit_product.html', context)


def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=product)
        if edit_form.is_valid():
            edited_product = edit_form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  # Redirect to the same page

    else:
        edit_form = ProductEditForm(instance=product)

    context = {
        'edit_form': edit_form,
        'product': product,
    }

    return render(request, 'edit_product.html', context)