from django.shortcuts import render,redirect
from .models import PracticeData
from django.http import HttpResponse
def mainpage(request):
    employee=PracticeData.objects.all()
    return render(request,'mainpage.html',{'xyz':employee})
def homepage(request):
    if request.method=='GET':
        return render(request,'home.html')
    else:
        PracticeData(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        contact=request.POST['contact'],
        course=request.POST['course'],
        fee=request.POST['fee']

        ).save()
        return redirect(mainpage)

def successful(request,id):
    data=PracticeData.objects.filter(id=id)
    return render(request,'submition.html',{'xyz':data})

def submitation(request):
    return render(request,'successful.html')
