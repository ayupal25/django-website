from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.

def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')


def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')
