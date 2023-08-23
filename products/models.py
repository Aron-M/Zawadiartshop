from cloudinary.models import CloudinaryField
from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image')
    artist = models.CharField(max_length=100)
    origin = models.CharField(max_length=50)
    origin_image = CloudinaryField('origin_image')
    origin_code = models.CharField(max_length=3)
    style = models.CharField(max_length=50, default="Unknown")
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.name

