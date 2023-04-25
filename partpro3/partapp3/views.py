from django.shortcuts import render
from .models import ApplicationForm
def startinpage(request):
    return render(request,'statingpage.html')

def homepage(request):
    return render(request,'homepage.html')

def Applypage(request):
    return render(request,'Applypage.html')
