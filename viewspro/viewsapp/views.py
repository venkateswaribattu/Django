from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    x='welcome to friends forver'
    return HttpResponse(x)
