from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')
# Create your views here.
