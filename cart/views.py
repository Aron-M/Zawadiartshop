from django.shortcuts import get_object_or_404, render, redirect
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

    return render(request, 'cart.html', {'cart_items': cart_items, 'cart_total': cart_total})
    

def add_to_cart(request, product_id):
    # Get the product based on the product_id
    product = get_object_or_404(Product, id=product_id)

    # Retrieve the session key
    session_key = request.session.session_key

    # Create or get the cart associated with the session
    cart, created = Cart.objects.get_or_create(session=session_key)

    # Check if the product is already in the cart
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    # If the item was already in the cart, increase its quantity by 1
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    # Redirect to the cart view or any other appropriate view
    return redirect('cart:cart_view')


def remove_from_cart(request, cart_item_id):
    # Get the current user's session
    session_key = request.session.session_key
    session = Session.objects.get(session_key=session_key)

    # Retrieve the user's cart for this session
    cart = Cart.objects.get(session=session)

    # Remove the selected item from the cart
    CartItem.objects.filter(cart=cart, id=cart_item_id).delete()

    return redirect('cart:remove_from_cart')
