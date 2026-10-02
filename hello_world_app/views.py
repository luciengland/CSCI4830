from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello, world!")

def index(request):
    return render(request, 'index_hello.html')

def about(request):
    return render(request, 'about_hello.html')