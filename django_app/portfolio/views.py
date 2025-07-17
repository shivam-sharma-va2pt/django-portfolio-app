from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Shivam Portfolio</h1><p>Complfdhgete Hoogaya</p>")
# Create your views here.
