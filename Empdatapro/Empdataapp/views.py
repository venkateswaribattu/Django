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
