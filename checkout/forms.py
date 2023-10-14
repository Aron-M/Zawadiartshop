from django import forms


class DeliveryAddressForm(forms.Form):
    full_name = forms.CharField(max_length=100, label='Full Name')
    address_line1 = forms.CharField(max_length=255, label='Address Line 1')
    address_line2 = forms.CharField(max_length=255, required=False, label='Address Line 2')
    city = forms.CharField(max_length=100, label='City')
    state = forms.CharField(max_length=100, label='State/Province')
    postal_code = forms.CharField(max_length=10, label='Postal Code')
    country = forms.CharField(max_length=100, label='Country')
    phone_number = forms.CharField(max_length=20, label='Phone Number')