from django.shortcuts import render
from django.http import HttpResponse

def display(request):
    return HttpResponse("<h1>hola mundo!</h1>")

def display(request):
    return HttpResponse("<h2>hola mundo!</h2>")

# Create your views here.
