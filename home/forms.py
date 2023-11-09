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

ORIGIN_CHOICES = (
    ('Senegal', 'Senegal'),
    ('Kenya', 'Kenya'),
    ('Ghana', 'Ghana'),
    ('Nigeria', 'Nigeria'),
    ('Sierra Leone', 'Sierra Leone'),
    ('Tanzania', 'Tanzania'),
    ('South Africa', 'South Africa'),
)

class ProductEditForm(forms.ModelForm):
    # Modify the category field to use a ChoiceField with choices
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    origin = forms.ChoiceField(choices=ORIGIN_CHOICES)

    class Meta:
        model = Product
        fields = ['name', 'description', 'artist', 'style', 'origin', 'origin_image', 'price', 'image', 'category']

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance', None)
        super(ProductEditForm, self).__init__(*args, **kwargs)

        if instance:
            for field_name, field in self.fields.items():
                if field_name != 'image':
                    field.required = True