from django.http import HttpResponse

# Create your view here
def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')
