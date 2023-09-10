from django.db import models
from django.contrib.sessions.models import Session
from products.models import Product


class Cart(models.Model):
    session = models.OneToOneField(Session, on_delete=models.CASCADE, default=None)
    products = models.ManyToManyField(Product, through='CartItem')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
