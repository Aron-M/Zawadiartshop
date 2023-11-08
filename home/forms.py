# forms.py
from django import forms
from products.models import Product


class ProductSearchForm(forms.Form):
    id = forms.IntegerField(label='Product ID', required=True)


CATEGORY_CHOICES = (
    ('Paintings', 'Paintings'),
    ('Sculptures', 'Sculptures'),
    ('Frames', 'Frames'),
    ('Crafts', 'Crafts'),
)

class ProductEditForm(forms.ModelForm):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ['name', 'description', 'artist', 'style', 'origin', 'price', 'image', 'origin_code', 'stock', 'category']