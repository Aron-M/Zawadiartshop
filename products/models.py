from cloudinary.models import CloudinaryField
from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('paintings', 'Paintings'),
        ('sculptures', 'Sculptures'),
        ('frames', 'Frames'),
        ('crafts', 'Crafts'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image')
    artist = models.CharField(max_length=100)
    origin = models.CharField(max_length=50)
    origin_image = CloudinaryField('origin_image')
    style = models.CharField(max_length=50, default="Unknown")
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

