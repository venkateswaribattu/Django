from django.http import HttpResponse
from django.shortcuts import render
import faker
fake=faker.Faker()
from .models import EmployeeData

def emplayeedataView(request):
    for i in range(100):
        EmployeeData(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        email=fake.email(),
        salary=fake.random_element(elements=(10000,20000,30000,40000)),
        company=fake.random_element(elements=('TCS', 'WIPRO', 'INFOSYS', 'HCL')),
        location=fake.random_element(elements=('Hydarabad','Bangalor','Chennai','Pune')),
        address=fake.address()
        ).save()
    return HttpResponse('Data saved')


def fetchingalldata(request):
    employees=EmployeeData.objects.all()
    return render(request,'employeesdata.html',{'employees':employees})

def mainPage(request):
    return render(request,'mainPage.html')

def hyderabaddata(request):
    if request.method=='GET':
        hydData=EmployeeData.objects.filter(location='Hydarabad')
        return render(request,'hydData.html',{'Data':hydData})
    else:
        company=request.POST.get('company')
        hydData=EmployeeData.objects.filter(location='Hydarabad')&EmployeeData.objects.filter(company=company)
        return render(request,'hydData.html',{'Data':hydData})

def bangdata(request):
    if request.method=='GET':
        bangData=EmployeeData.objects.filter(location='Bangalor')
        return render(request,'bangData.html',{'Data':bangData})
    else:
        company=request.POST.get('company')
        bangData=EmployeeData.objects.filter(location='Bangalor')&EmployeeData.objects.filter(company=company)
        return render(request,'bangData.html',{'Data':bangData})
def chedata(request):
    if request.method=='GET':
        cheData=EmployeeData.objects.filter(location='Chennai')
        return render(request,'cheData.html',{'Data':cheData})
    else:
        company=request.POST.get('company')
        cheData=EmployeeData.objects.filter(location='Chennai')&EmployeeData.objects.filter(company=company)
        return render(request,'cheData.html',{'Data':cheData})
def punedata(request):
    if request.method=='GET':
        puneData=EmployeeData.objects.filter(location='Pune')
        return render(request,'puneData.html',{'Data':puneData})
    else:
        company=request.POST.get('company')
        puneData=EmployeeData.objects.filter(location='Pune')&EmployeeData.objects.filter(company=company)
        return render(request,'puneData.html',{'Data':puneData})
