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
    class Meta:
        model = Product
        fields = ['name', 'description', 'artist', 'style', 'origin', 'price', 'image', 'origin_code', 'stock', 'category']

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        super(ProductEditForm, self).__init__(*args, **kwargs)

        if instance:
            for field_name, field in self.fields.items():
                if field_name != 'image':
                    field.required = True