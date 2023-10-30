from django.shortcuts import render, redirect
from .forms import DeliveryAddressForm
from cart.models import Cart, CartItem
from .models import Order
from products.models import Product
from django.db.models import Sum
from django.shortcuts import render, redirect, reverse
from django.contrib import messages


def checkout_view(request):
    if request.method == 'POST':
        form = DeliveryAddressForm(request.POST)
        if form.is_valid():

            order = Order(
                user=request.user,  
                delivery_address=form.cleaned_data['delivery_address'],

            )
            order.save()

            return redirect('checkout:confirmation') 
    else:
        form = DeliveryAddressForm()
    
    session_key = request.session.session_key

    if session_key:
        cart_items = CartItem.objects.filter(cart__session=session_key)

        
        for cart_item in cart_items:
            cart_item.total = cart_item.product.price * cart_item.quantity

        cart_total = sum(cart_item.total for cart_item in cart_items)

        
        def calculate_total_products():
            return cart_items.aggregate(total_products=Sum('quantity'))['total_products']

        total_products = calculate_total_products()
    else:
        cart_items = []
        cart_total = 0
        total_products = 0
    
    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
        'total_products': total_products,
        'form': form,
        'stripe_public_key': 'pk_test_51NYBbGBUqkswIymkiNneN1yZ4ohRjxnMWsJCQVC3JymwTxXyEkxcNZ4gWQXcFNXOcKNF0Su4TKXft13HI97SSxBF008fmQ2ySj',
        'client_secret': 'test client secret',
    }
    
    return render(request, 'checkout.html', context)


def checkout_product_view(request):
    session_key = request.session.session_key

    if session_key:
        cart_items = CartItem.objects.filter(cart__session=session_key)

        
        for cart_item in cart_items:
            cart_item.total = cart_item.product.price * cart_item.quantity

        cart_total = sum(cart_item.total for cart_item in cart_items)

        
        def calculate_total_products():
            return cart_items.aggregate(total_products=Sum('quantity'))['total_products']

        total_products = calculate_total_products()
    else:
        cart_items = []
        cart_total = 0
        total_products = 0
    
    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
        'total_products': total_products,
    }

    return render(request, 'checkout.html', context)


def confirmation_view(request):
    return render(request, 'checkout/checkout_confirmation.html')

