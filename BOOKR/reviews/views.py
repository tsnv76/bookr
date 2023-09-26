from django.http import HttpResponse
from django.shortcuts import render

from .models import Book


def index(request):
    name = 'Bob!'
    return render(request, "base.html", {"name": name})

def welcome_view(request):
    message = f'<html><h1>Welcome to Bookr!</h1!>' \
              f'<p>{Book.objects.count()} books and counting! </p></html>'
    return HttpResponse(message)
