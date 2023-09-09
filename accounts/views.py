# accounts/views.py
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required



def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_profile')
    else:
        form = RegistrationForm()
    return render(request, '/workspace/Zawadiartshop/accounts/templates/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_profile')
    else:
        form = LoginForm()
    return render(request, '/workspace/Zawadiartshop/accounts/templates/login.html', {'form': form})


@login_required
def user_profile(request):
    return render(request, 'userprofile.html', {'user': request.user})


def logout_view(request):
    logout(request)
    return redirect('/workspace/Zawadiartshop/home/templates/homepage.html')  # Redirect to your home page
