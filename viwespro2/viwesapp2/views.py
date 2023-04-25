from django.shortcuts import render

from django.http import HttpResponse
def namepage(request):
    x='welcome to my family'
    return HttpResponse(x) 
