from django.shortcuts import render, redirect

from .models import EmpData
def homePage(request):
    emps=EmpData.objects.all()
    return render (request,'homePage.html',{'abc':emps})
def addingemp(request):
    if request.method=='GET':
        return render(request,'addEmp.html')
    else:
        EmpData(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        email=request.POST['email'],
        mobile=request.POST['mobile'],
        company=request.POST['company'],
        salary=request.POST['salary'],
        expirence=request.POST['expirence']

        ).save()
        return redirect(homePage)
