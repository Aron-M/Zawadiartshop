from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm, CustomLoginForm
from checkout.forms import DeliveryAddressForm
from checkout.models import Order
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import logging


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_profile')
    else:
        form = RegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})


logger = logging.getLogger(__name__)


def custom_login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('welcome_back')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = CustomLoginForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def user_profile(request):
    return render(request, 'registration/userprofile.html', {'user': request.user})


def welcome_back(request):
    return render(request, 'registration/welcome_back.html', {'user': request.user})


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('products:home')


@login_required
def update_user_address(request):
    if request.method == 'POST':
        form = DeliveryAddressForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('user_profile')
    else:
        form = DeliveryAddressForm()
        print(form)  # Add this line for debugging
    return render(request, 'registration/userprofile.html', {'form': form})
