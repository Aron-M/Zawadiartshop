from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def homepage_view(request):
    # Render the homepage template
    return render(request, 'home/templates/homepage.html')