from django.db import models
from products.models import Product  # Import your Product model from your main app


class CartItem(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  # If you have user authentication
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

