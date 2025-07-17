from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Shivam's Portfolio</h1><p>This is my first Django project!</p>")
# Create your views here.
