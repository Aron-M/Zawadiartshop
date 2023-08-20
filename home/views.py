from django.shortcuts import render

# Create your views here.


def homepage_view(request):
    # Render the homepage template
    return render(request, 'homepage.html')