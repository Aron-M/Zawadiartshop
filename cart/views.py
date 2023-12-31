from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.sessions.models import Session
from cart.models import Cart, CartItem
from django.http import HttpResponse
from products.models import Product
from django.db.models import Sum


def calculate_cart_total(cart_items):
    return cart_items.aggregate(total_products=Sum('quantity'))['total_products'] or 0


def cart_view(request):
    session_key = request.session.session_key

    if session_key:
        cart_items = CartItem.objects.filter(cart__session=session_key)

        # Calculate the total for each item and add it to the cart_item objects
        for cart_item in cart_items:
            cart_item.total = cart_item.product.price * cart_item.quantity

        cart_total = sum(cart_item.total for cart_item in cart_items)

        # Function to calculate the total number of products
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

    return render(request, 'cart.html', context)


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

    # Prepare the alert message
    alert_message = "Product successfully added to the cart."

    # Pass the alert message to the template
    return render(request, 'product_search.html', {'alert_message': alert_message})


def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('cart:cart_view')


def update_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)

    if request.method == 'POST':
        new_quantity = int(request.POST['quantity'])

        if new_quantity > 0:
            cart_item.quantity = new_quantity
            cart_item.save()

    return redirect('cart:cart_view')