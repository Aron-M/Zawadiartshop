# forms.py
from django import forms
from products.models import Product


class ProductSearchForm(forms.Form):
    id = forms.IntegerField(label='Product ID', required=True)