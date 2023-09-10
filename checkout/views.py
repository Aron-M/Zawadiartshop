from django.shortcuts import render, redirect
from .forms import DeliveryAddressForm
from .models import Order

def checkout_view(request):
    if request.method == 'POST':
        form = DeliveryAddressForm(request.POST)
        if form.is_valid():

            order = Order(
                user=request.user,  
                delivery_address=form.cleaned_data['delivery_address'],

            )
            order.save()

            return redirect('checkout:confirmation') 
    else:
        form = DeliveryAddressForm()

    return render(request, 'checkout/checkout.html', {'form': form})

def confirmation_view(request):
    # You can fetch order details here to display on the confirmation page
    # For example, you can retrieve the most recent order for the logged-in user
    # and pass it to the template
    return render(request, 'checkout/checkout_confirmation.html')

