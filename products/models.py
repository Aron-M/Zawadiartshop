from django.db import models
from cloudinary.models import CloudinaryField


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image')
    artist = models.CharField(max_length=100)
    origin = models.CharField(max_length=50)
    origin_image = CloudinaryField('origin_image')
    origin_code = models.CharField(max_length=3)
    style = models.CharField(max_length=50, default="Unknown")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.CharField(max_length=20)
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.name
