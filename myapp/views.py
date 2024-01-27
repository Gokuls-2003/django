from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    content = "<html><body><h1>Welcome to little lemon</h></body></html>"
    return HttpResponse(content)
