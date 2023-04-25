from django.shortcuts import render,redirect
from .models import StudentData
def homePage(request):
    stu=StudentData.objects.all()
    return render(request,'mainPage.html',{'abc':stu})
def mainPage(request):
    if request.method =='GET':
        return render(request,'homePage.html')
    else:
        StudentData(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        email=request.POST['email'],
        mobile=request.POST['mobile'],
        course=request.POST['course'],
        fee=request.POST['fee'],
        location=request.POST['location'],
        institute=request.POST['institute']

        ).save()
        return redirect(homePage)
def featchingdata(request,id):
    students=StudentData.objects.filter(id=id)
    return render(request,'studentdata.html',{'abc':students})
