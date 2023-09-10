from django.db.models import Sum
from .models import CartItem

def cart_info(request):
    user = request.user
    cart_items = CartItem.objects.filter(cart__session=request.session.session_key)

    total_products = 0
    for cart_item in cart_items:
        total_products += cart_item.quantity

    return {
        'username': user.username if user.is_authenticated else '',
        'total_products': total_products,
    }