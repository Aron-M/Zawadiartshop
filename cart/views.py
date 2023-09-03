# views.py

from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from .models import Cart, CartItem

def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)

    # Get the current user's session
    session_key = request.session.session_key
    session = Session.objects.get(session_key=session_key)

    # Check if a cart already exists for this session, create one if not
    cart, created = Cart.objects.get_or_create(session=session)

    # Check if the product is already in the cart; if so, increment the quantity
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart:cart', product_id=product_id)


def remove_from_cart(request, cart_item_id):
    # Get the current user's session
    session_key = request.session.session_key
    session = Session.objects.get(session_key=session_key)

    # Retrieve the user's cart for this session
    cart = Cart.objects.get(session=session)

    # Remove the selected item from the cart
    CartItem.objects.filter(cart=cart, id=cart_item_id).delete()

    return redirect('cart:cart')
