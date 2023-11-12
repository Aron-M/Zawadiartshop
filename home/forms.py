# forms.py
from django import forms
from products.models import Product
from django.utils.safestring import mark_safe

class ProductSearchForm(forms.Form):
    id = forms.IntegerField(label='Product ID', required=True)


class ProductEditForm(forms.ModelForm):
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

    ORIGIN_IMAGE_CHOICES = (
        ('Senegal', 'https://res.cloudinary.com/dj3upv8lw/image/upload/v1692523461/flag%20icons/senegal_kb0bag.png'),
        ('Kenya', 'https://res.cloudinary.com/dj3upv8lw/image/upload/v1692523654/flag%20icons/kenya_cgsacm.png'),
        ('Ghana', 'https://res.cloudinary.com/dj3upv8lw/image/upload/v1692523461/flag%20icons/ghana_ty7sif.png'),
        ('Nigeria', 'https://res.cloudinary.com/dj3upv8lw/image/upload/v1692523461/flag%20icons/nigeria_zxyhb4.png'),
        ('Sierra Leone', 'https://res.cloudinary.com/dj3upv8lw/image/upload/v1692523491/flag%20icons/sierra-leone_tkvubf.png'),
        ('Tanzania', 'https://res.cloudinary.com/dj3upv8lw/image/upload/v1692523461/flag%20icons/tanzania_pi6tn0.png'),
        ('South Africa', 'https://res.cloudinary.com/dj3upv8lw/image/upload/v1692523461/flag%20icons/south-africa_1_hyh59u.png'),
    )

    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    origin = forms.ChoiceField(choices=ORIGIN_CHOICES)
    origin_image = forms.ChoiceField(choices=ORIGIN_IMAGE_CHOICES)

    class Meta:
        model = Product
        fields = ['name', 'description', 'artist', 'style', 'origin', 'origin_image', 'price', 'image', 'category']

    # No need for __init__ and clean_origin_image

    def add_images_to_choices(self, choices):
        return [
            (value, mark_safe(f'<img src="{image_url}" alt="{value}" width="100" height="100">'))
            for value, image_url in choices
        ]






