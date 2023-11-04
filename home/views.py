from django.shortcuts import render


def dashboard_view(request):
    return render(request, '/workspace/Zawadiartshop/home/templates/dashboard.html')