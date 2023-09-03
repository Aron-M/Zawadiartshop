# views.py

from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from .models import Cart, CartItem
from products.models import Product


def cart_view(request):
    session_key = request.session.session_key

    if session_key:
        cart_items = CartItem.objects.filter(cart__session=session_key)
        cart_total = sum(item.product.price * item.quantity for item in cart_items)
    else:
        cart_items = []
        cart_total = 0

    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'cart_total': cart_total})
    

def add_to_cart(request, product_id):
    # Get the product based on the product_id from the URL
    product = get_object_or_404(Product, pk=product_id)

    # Get or create the user's cart based on their session
    session_key = request.session.session_key
    if not session_key:
        request.session.save()
        session_key = request.session.session_key

    cart, created = Cart.objects.get_or_create(session=session_key)

    # Check if the product is already in the cart; if so, update quantity
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart:add_to_cart')


def remove_from_cart(request, cart_item_id):
    # Get the current user's session
    session_key = request.session.session_key
    session = Session.objects.get(session_key=session_key)

    # Retrieve the user's cart for this session
    cart = Cart.objects.get(session=session)

    # Remove the selected item from the cart
    CartItem.objects.filter(cart=cart, id=cart_item_id).delete()

    return redirect('cart:cart')
