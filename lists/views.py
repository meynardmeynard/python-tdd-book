from django.shortcuts import render

# Create your view here
def home_page(request):
    return render(request, 'home.html')
