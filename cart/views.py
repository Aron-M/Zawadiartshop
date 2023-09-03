from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.sessions.models import Session
from cart.models import Cart, CartItem
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
    # Retrieve the product by its ID or return a 404 response if not found
    product = get_object_or_404(Product, id=product_id)

    # Get or create the user's session
    session_key = request.session.session_key
    if not session_key:
        request.session.save()
        session_key = request.session.session_key

    # Get or create the user's cart
    cart, created = Cart.objects.get_or_create(session_id=session_key)

    # Check if the product is already in the cart
    cart_item, created = cart.cartitem_set.get_or_create(product=product)

    # If the product is already in the cart, increment its quantity by 1
    if not created:
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

    return redirect('cart:remove_from_cart')
