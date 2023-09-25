from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    name = 'Bob!'
    return render(request, "base.html", {"name": name})
