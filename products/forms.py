from django import forms
from .models import Product


class ProductFilterForm(forms.Form):
    CATEGORY_CHOICES = [
        ('', 'All'),
        ('paintings', 'Paintings'),
        ('sculptures', 'Sculptures'),
        ('frames', 'Frames'),
        ('crafts', 'Crafts'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=False)
    artist = forms.CharField(max_length=100, required=False)
    origin = forms.CharField(max_length=50, required=False)
    max_price = forms.DecimalField(max_digits=8, decimal_places=2, required=False)
