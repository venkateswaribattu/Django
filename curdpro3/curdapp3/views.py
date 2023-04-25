from django.shortcuts import render,redirect

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
        location=request.POST['location'],
        expirence=request.POST['expirence']

        ).save()
        return redirect(homePage)
def update(request, id):
    emp=EmpData.objects.get(id=id)
    return render(request,'update.html',{'emp':emp})

def updating_emp(request,id):
    emp=EmpData.objects.get(id=id)
    emp.first_name=request.POST['fname']
    emp.last_name=request.POST['lname']
    emp.email=request.POST['email']
    emp.mobile=request.POST['mobile']
    emp.company=request.POST['company']
    emp.salary=request.POST['salary']
    emp.location=request.POST['location']
    emp.expirence=request.POST['expirence']
    emp.save()
    return redirect(homePage)


def delete(request,id):
    emp=EmpData.objects.get(id=id)
    emp.delete()
    return redirect(homePage)
