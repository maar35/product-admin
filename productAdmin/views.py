from django.shortcuts import render
from django.http import HttpResponse


# Polls view.


def index(request):
    return HttpResponse("Hi folks! Welcome back at our product administration.")
