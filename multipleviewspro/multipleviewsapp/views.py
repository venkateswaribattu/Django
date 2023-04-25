from django.shortcuts import render

from django.http import HttpResponse
def homepage(request):
    x='Welcome to nth home'
    return HttpResponse(x)
def contactpage(request):
    x='our contact number 9704790746'
    return HttpResponse(x)
def feadbackpage(request):
    x='we have good feadback'
    return HttpResponse(x)
def gallarypage(request):
    x='we have so many photos in gallary'
    return HttpResponse(x)
