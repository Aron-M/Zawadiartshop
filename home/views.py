from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .forms import ProductSearchForm, ProductEditForm

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
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, instance=product)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('dashboard')
        else:
            print(edit_form.errors)
            print(request.POST)
    else:
        edit_form = ProductEditForm(instance=product)

    return render(request, 'dashboard.html', {'edit_form': edit_form, 'product': product})
