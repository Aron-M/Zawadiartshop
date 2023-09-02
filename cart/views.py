# cart/views.py

from django.shortcuts import render
from .models import CartItem

def cart_view(request):
    cart_items = CartItem.objects.all()  # Assuming you have user authentication

    # Calculate the total for each cart item and update the CartItem instances
    for item in cart_items:
        item.total = item.product.price * item.quantity

    # Calculate the overall cart total
    cart_total = sum(item.total for item in cart_items)

    return render(request, 'cart.html', {'cart_items': cart_items, 'cart_total': cart_total})


