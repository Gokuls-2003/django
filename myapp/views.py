from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from datetime import datetime

def home(request):
    content = "<html><body><h1>Welcome to little lemon</h></body></html>"
    return HttpResponse(content)


def say_hello(request):
    return HttpResponse("Hello all")

def displayDate(request):
    date_joined =datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text = """<h1 style="color: #F4CE14:">THIS IS LITTLE LEMON AGAIN!</h1>"""
    return HttpResponse(text)