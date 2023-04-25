from django.shortcuts import render

from django.http import HttpResponse
def contactpage(request):
    x='welcome to vindhya tech house'
    return HttpResponse(x)
