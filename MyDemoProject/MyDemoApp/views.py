from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myApp(request):
    return HttpResponse('<h1>This is my first Django App!</h1>')
