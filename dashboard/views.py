from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

post = [
    {

    }
]

def index(request):
    return render(request, 'pages/dashboard.html')

def boxes(request):
    return render(request, 'pages/boxes.html')

def connection(request):
    return render(request, 'pages/connection.html')

def base(request):
    return render(request, 'pages/base.html')